from flask import Request, Response
from typing import Callable, Any
from infra.db.db_context import Connection, execute_connect
from infra.dependency_injector import container
from traceback import format_exc


def services_decorator(request: Request, data_base: str, type_service: str) -> Callable:
    
    def get_service(container: tuple, type_service: str) -> dict | None:

        costumer, products = container

        match type_service:
            case 'COSTUMER':
                service = costumer
            case 'PRODUCTS':
                service = products
            case _:
                service: dict | None = {}

        return service

    def get_method(methods: str) -> dict | None:

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
            case _:
                params: dict | None = None

        return params

    def decorator(func: Callable) -> Callable:

        def wrapper() -> Response:

            conn: Connection | None = None

            result: dict = {}

            try:

                conn = execute_connect(data_base)

                result = func(get_method(request.method.upper()),
                                services=get_service(container(conn.cursor()), type_service))

            except Exception:
                # TODO: Criar funcionalidade para armazenar log de erros
                print(format_exc())
                result.update({"data": "Erro no servidor", "status_code": 500})
                if conn:
                    conn.rollback()
            else:
                conn.commit()
            finally:

                if conn:
                    conn.close()

                return Response(result["data"],
                                status=result["status_code"],
                                mimetype='application/json')

        return wrapper

    return decorator
