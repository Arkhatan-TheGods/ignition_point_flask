import database_query
# from typing import TypedDict, Callable, Any

def costumer_repository(repository: dict) -> dict:

    def add(costumer: tuple) -> tuple:
        return repository['execute']("INSERT INTO COSTUMERS(NAME, \
                                     CPF, BIRTH_DATE, ADDRESS) \
                                     VALUES(:NAME, :CPF, :BIRTH_DATE, :ADDRESS);", costumer)

    def get_by_id(id: int) -> tuple:

        return repository["fetchone"]("SELECT ID, NAME, CPF, BIRTH_DATE, ADDRESS \
                                      FROM COSTUMERS WHERE ID =: $ID;", id)

    def get_by_name(name: str) -> tuple:
        
        return repository['fetchall']("SELECT ID, NAME, CPF, BIRTH_DATE, ADDRESS \
                                      FROM CLIENTE WHERE LOWER(NAME) =: $NAME AND LIMIT 10;", name)

    def get_by_cpf(cpf: str) -> tuple:

        return repository["fetchone"]("SELECT ID, NAME, CPF, BIRTH_DATE, \
                                      ADDRESS FROM COSTUMERS WHERE CPF =: $CPF;", cpf)

    def update_costumer_by_id(values: tuple) -> None:
        query = database_query.update_costumer()
        return repository['execute'](query, values)

    def delete_costumer_by_id(id:int) -> None:
        query = database_query.delete_costumer()
        return repository['execute'](query, id)

    def get_all() -> list[tuple]:
        return repository['all']("SELECT * FROM COSTUMERS;")

    return {'add': add,
            'get_costumer_by_id': get_by_id,
            'get_costumer_by_name': get_by_name,
            'get_by_cpf': get_by_cpf,
            'update_costumer': update_costumer_by_id,
            'delete_costumer': delete_costumer_by_id,
            'all': get_all}
