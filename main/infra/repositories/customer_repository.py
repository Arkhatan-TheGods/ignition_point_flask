def customer_repository(repository: dict) -> dict:

    def add(customer: tuple) -> tuple:

        return repository['execute']("""INSERT INTO CUSTOMER(NAME, CPF, BIRTH_DATE, ADDRESS) 
        VALUES(:NAME, :CPF, :BIRTH_DATE, :ADDRESS);""", customer)

    def get_by_id(customer_id: int) -> tuple:

        return repository["fetchone"]("SELECT ID, NAME, CPF, BIRTH_DATE, ADDRESS \
                                      FROM CUSTOMER WHERE ID = :ID;", customer_id)

    def get_all() -> list[tuple]:
        return repository['all']("SELECT * FROM customer;")

    def get_by_name(name: str) -> tuple:
        
        return repository['fetchall']("SELECT ID, NAME, CPF, BIRTH_DATE, ADDRESS \
                                      FROM CUSTOMER WHERE LOWER(NAME) = '%:NAME' AND LIMIT 10;", name)

    def get_by_cpf(cpf: str) -> tuple:

        return repository["fetchone"]("SELECT ID, NAME, CPF, BIRTH_DATE, \
                                      ADDRESS FROM CUSTOMER WHERE CPF = :CPF;", cpf)

    def edit(values: tuple) -> None:
        return repository['execute']("", values)

    def remove(id:int) -> None:
        return repository['execute']("", id)


    return {'add': add,
            'get_customer_by_id': get_by_id,
            'get_customer_by_name': get_by_name,
            'get_by_cpf': get_by_cpf,
            'edit': edit,
            'remove': remove,
            'all': get_all}
