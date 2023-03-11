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
        

    def get_costumer_by_id(id: int) -> tuple[str,str,str,str]:
        query = database_query.find_costumer_by_id()
        return operation['fetchone'](query,id)
    

    def show_all_costumer() -> list[tuple]:
        query = database_query.all_costumer()
        return operation['all'](query)
