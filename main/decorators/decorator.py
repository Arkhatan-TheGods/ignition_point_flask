from flask import Request
from typing import Callable, Any
from infra.db.db_context import Connection, execute_connect
from infra.dependency_injector import container
from traceback import format_exc


def services_decorator(request: Request, data_base: str, type_service: str) -> Callable:

    def decorator(func: Callable) -> Callable:

        def wrapper(*args, **kwargs) -> dict:

            conn: Connection | None = None

            response: dict = {}

            try:

                conn = execute_connect(data_base)

                costumer, products = container(conn.cursor())

                service: dict = {}

                match type_service:
                    case 'COSTUMER':
                        service = costumer
                    case 'PRODUCTS':
                        service = products

                params:dict = {}
                
                match request.method.upper():
                    case 'POST':
                        params = {"data": request.get_json()}
                    case 'GET':
                        params = {"args": request.args.get("id", "")}
                    case 'PUT':
                        params = {"args": request.args.get("id", ""),
                                  "data": request.get_json()}
                    case 'DELETE':
                        params = {"args": request.args.get("id", "")}

                response = func(*args, **params, **service, **kwargs)

            except Exception:
                # TODO: Criar funcionalidade para armazenar log de erros
                print(format_exc())

                if conn:
                    conn.rollback()
            else:
                conn.commit()
                jsonify({"consumer": response})
            finally:

                if conn:
                    conn.close()

                return response

        return wrapper

    return decorator
