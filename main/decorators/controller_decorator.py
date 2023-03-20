from flask import Response
from typing import Callable
from infra.db.db_context import Connection, execute_connect
from traceback import format_exc


def controller_decorator(type_service: str, parameters: tuple) -> Callable:

    get_service, data_base, container = parameters

    def decorator(func: Callable) -> Callable:

        def wrapper() -> Response:
            
            conn: Connection | None = None
            
            message_error: str | None = None
            
            status_code: int | None = None

            result: dict = {}

            try:

                conn = execute_connect(data_base)

                result = func(get_service(container(conn.cursor()), type_service))

            except Exception as ex:
                # TODO: Criar funcionalidade para armazenar log de erros
                # print(format_exc())
                if  type(ex.args) == tuple:

                    message_error = ex.args[0]
                    status_code = ex.args[1]
                else:
                    message_error = "Server Error"
                    status_code = 500
                if conn:
                    conn.rollback()
            else:
                conn.commit()
            finally:

                if conn:
                    conn.close()

                return Response(response=message_error if message_error else result[0],
                                status=status_code if status_code else result[1],
                                mimetype='application/json')

        return wrapper

    return decorator
