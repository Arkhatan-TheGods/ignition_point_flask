from flask import Request
from typing import Callable, Any
from infra.db.db_context import Connection, execute_connect
from infra.dependency_injector import container
from traceback import format_exc


def services_decorator(request: Request, data_base: str, type_service: str) -> Callable:

    def get_service(container:tuple, type_service: str) -> dict | None:
        
        costumer, products = container
        
        service: dict | None = {}
        match type_service:
            case 'COSTUMER':
                service = costumer
            case 'PRODUCTS':
                service = products
        return service

    def get_method(methods: str) -> dict | None:
        params: dict | None = {}
        match methods:
            case 'POST':
                params = {"data": request.get_json()}
            case 'GET':
                params = {"id": request.args.get("id", "")}
            case 'PUT':
                params = {"id": request.args.get("id", ""),
                            "data": request.get_json()}
            case 'DELETE':
                params = {"id": request.args.get("id", "")}

        return params


    def decorator(func: Callable) -> Callable:

        def wrapper() -> dict:

            conn: Connection | None = None

            response: dict = {}

            try:

                conn = execute_connect(data_base)

                response = func(get_method(request.method.upper()),
                                services=get_service(container(conn.cursor()), type_service))

            except Exception:
                # TODO: Criar funcionalidade para armazenar log de erros
                print(format_exc())

                if conn:
                    conn.rollback()
            else:
                conn.commit()
            finally:

                if conn:
                    conn.close()

                return response

        return wrapper

    return decorator
