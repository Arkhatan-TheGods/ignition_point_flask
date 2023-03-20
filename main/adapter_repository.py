import database_query
from typing import TypedDict, Callable, Any


# Operation = TypedDict('Operation',
#                       {'execute': Callable[[str, tuple], Any],
#                        'fetchone': Callable[[str, tuple], Any],
#                        'fetchall': Callable[[str, tuple], Any]})


def costumer(operation: dict) -> dict:
    def new_costumer(values: tuple) -> None:
        query = database_query.new_customer()
        return operation['execute'](query, values)

    def get_costumer_by_id(id: int) -> tuple[int, str, str, str, str]:
        query = database_query.find_customer_by_id()
        return operation['fetchone'](query, id)

    def get_costumer_by_name(name: str) -> tuple[int, str, str, str, str]:
        query = database_query.find_customer_by_name()
        return operation['fetchall'](query, name)

    def find_costumer_by_cpf(cpf: str) -> tuple:
        query = database_query.find_customer_by_cpf()
        return operation["fetchone"](query, cpf)

    def update_costumer_by_id(values: tuple) -> None:
        query = database_query.update_costumer()
        return operation['execute'](query, values)

    def delete_costumer_by_id(id:int) -> None:
        query = database_query.delete_costumer()
        return operation['execute'](query, id)

    def all() -> list[tuple]:
        query = database_query.all_costumer()
        return operation['all'](query)

    return {'new_costumer': new_costumer,
            'get_costumer_by_id': get_costumer_by_id,
            'get_costumer_by_name': get_costumer_by_name,
            'update_costumer': update_costumer_by_id,
            'delete_costumer': delete_costumer_by_id,
            'all': all}
