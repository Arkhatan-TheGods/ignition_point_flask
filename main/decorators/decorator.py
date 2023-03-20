from flask import Request, Response
from typing import Callable, Any
from infra.db.db_context import Connection, execute_connect
from traceback import format_exc


def services_decorator(type_service: str, parameters: tuple) -> Callable:

    # request, check_params, get_service, data_base, container = parameters
    get_service, data_base, container = parameters

    def decorator(func: Callable) -> Callable:

        def wrapper() -> Response:

            conn: Connection | None = None

            result: dict = {}

            try:

                conn = execute_connect(data_base)

                # result = func(check_params(request),
                #                 services=get_service(container(conn.cursor()), type_service))
                result = func(services=get_service(container(conn.cursor()), type_service))

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
