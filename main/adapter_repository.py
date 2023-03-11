import database_query
from typing import TypedDict, Callable, Any


Operation = TypedDict('Operation',
                      {'execute': Callable[[str, tuple], Any],
                       'fetchone': Callable[[str, tuple], Any],
                       'fetchall': Callable[[str, tuple], Any]})


def costumer(operation: Operation) -> dict:
    def new_costumer(values: tuple) -> None:
        query = database_query.new_costumer()
        return operation['execute'](query, values)
        pass

    def get_costumer_by_id(id: int) -> tuple:
        pass
