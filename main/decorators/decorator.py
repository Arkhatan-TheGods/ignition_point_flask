from typing import Callable
from infra.db.db_context import Connection, execute_connect
from infra.dependency_injector import container
from traceback import format_exc


def services_decorator(data_base: str, type_service: str) -> Callable:

    def decorator(func: Callable) -> Callable:

        def wrapper(*args, **kwargs) -> dict:

            print(">>>>>>>>>>>>args:", args)

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

                response = func(*args, **service, **kwargs)

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
