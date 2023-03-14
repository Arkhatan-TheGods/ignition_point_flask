import database_query
# from typing import TypedDict, Callable, Any

def costumer_repository(repository: dict) -> dict:

    def new_costumer(values: tuple) -> None:
        query = database_query.new_costumer()
        return repository['execute'](query, values)

    def get_costumer_by_id(id: int) -> tuple[int, str, str, str, str]:
        query = database_query.find_costumer_by_id()
        return repository['fetchone'](query, id)

    def get_costumer_by_name(name: str) -> tuple[int, str, str, str, str]:
        query = database_query.find_costumer_by_name()
        return repository['fetchall'](query, name)

    def find_costumer_by_cpf(cpf: str) -> tuple:
        query = database_query.find_costumer_by_cpf()
        return repository["fetchone"](query, cpf)

    def update_costumer_by_id(values: tuple) -> None:
        query = database_query.update_costumer()
        return repository['execute'](query, values)

    def delete_costumer_by_id(id:int) -> None:
        query = database_query.delete_costumer()
        return repository['execute'](query, id)

    def all() -> list[tuple]:
        return repository['all']("SELECT * FROM CLIENTE;")

    return {'new_costumer': new_costumer,
            'get_costumer_by_id': get_costumer_by_id,
            'get_costumer_by_name': get_costumer_by_name,
            'update_costumer': update_costumer_by_id,
            'delete_costumer': delete_costumer_by_id,
            'all': all}
