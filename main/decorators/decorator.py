from typing import Callable
from sqlite3 import Connection, connect
from infra.dependency_injector import container


def services_decorator(data_base: str, type_service: str) -> Callable:

    def decorator(func: Callable) -> Callable:

        def wrapper(*args, **kwargs) -> dict:

            conn: Connection = connect(data_base)

            service: dict = {}

            response: dict = {}

            try:

                costumer, products = container(conn.cursor())

            except Exception as ex:
                print("Erro", ex)

            else:

                try:
                    match type_service:
                        case 'COSTUMER':
                            service = costumer
                        case 'PRODUCTS':
                            service = products

                    response = func(*args, **service, **kwargs)

                except Exception as ex:
                    print("Erro", ex)
                    conn.rollback()
                else:
                    conn.commit()

            finally:
                conn.close()

                return response

        return wrapper

    return decorator
