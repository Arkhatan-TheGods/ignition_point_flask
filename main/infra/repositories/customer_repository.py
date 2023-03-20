import database_query

def customer_repository(repository: dict) -> dict:

    def add(customer: tuple) -> tuple:

        return repository['execute']("""INSERT INTO CUSTOMER(NAME, CPF, BIRTH_DATE, ADDRESS) 
        VALUES(:NAME, :CPF, :BIRTH_DATE, :ADDRESS);""", customer)

    def get_by_id(customer_id: int) -> tuple:

        return repository["fetchone"]("SELECT ID, NAME, CPF, BIRTH_DATE, ADDRESS \
                                      FROM CUSTOMER WHERE ID = :ID;", customer_id)

    def get_by_name(name: str) -> tuple:
        
        return repository['fetchall']("SELECT ID, NAME, CPF, BIRTH_DATE, ADDRESS \
                                      FROM CUSTOMER WHERE LOWER(NAME) = '%:NAME' AND LIMIT 10;", name)

    def get_by_cpf(cpf: str) -> tuple:

        return repository["fetchone"]("SELECT ID, NAME, CPF, BIRTH_DATE, \
                                      ADDRESS FROM CUSTOMER WHERE CPF = :CPF;", cpf)

    def update_customer_by_id(values: tuple) -> None:
        query = database_query.update_customer()
        return repository['execute'](query, values)

    def delete_customer_by_id(id:int) -> None:
        query = database_query.delete_customer()
        return repository['execute'](query, id)

    def get_all() -> list[tuple]:
        return repository['all']("SELECT * FROM customer;")

    return {'add': add,
            'get_customer_by_id': get_by_id,
            'get_customer_by_name': get_by_name,
            'get_by_cpf': get_by_cpf,
            'update_customer': update_customer_by_id,
            'delete_customer': delete_customer_by_id,
            'all': get_all}
