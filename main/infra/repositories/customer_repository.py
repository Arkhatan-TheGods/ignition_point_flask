def customer_repository(repository: dict) -> dict:

    def add(customer: tuple) -> tuple:

        return repository['execute']("INSERT INTO CUSTOMERS(NAME, CPF, BIRTH_DATE, ADDRESS) \
            VALUES(:NAME, :CPF, :BIRTH_DATE, :ADDRESS);", customer)

    def get_all() -> list[tuple]:
        return repository['all']("SELECT ID, NAME, CPF, BIRTH_DATE, ADDRESS \
                                 FROM CUSTOMERS;")

    def get_by_id(customer_id: tuple) -> tuple:

        customer = repository['fetchone']("SELECT ID, NAME, CPF, BIRTH_DATE, ADDRESS \
                                      FROM CUSTOMERS WHERE ID = :ID;", customer_id)

        return customer

    def get_by_cpf(cpf: tuple) -> tuple:

        return repository["fetchone"]("SELECT ID, NAME, CPF, BIRTH_DATE, \
                                      ADDRESS FROM CUSTOMERS WHERE CPF = :CPF;", cpf)

    def get_by_name(name: str) -> tuple:
        
        return repository['fetchall']("SELECT ID, NAME, CPF, BIRTH_DATE, ADDRESS \
                                      FROM CUSTOMERS WHERE LOWER(NAME) = '%:NAME' AND LIMIT 10;", name)


    def edit(values: tuple) -> None:
        return repository['execute']("", values)

    def remove(id:int) -> None:
        return repository['execute']("", id)


    return {'add': add,
            'all': get_all,
            'get_by_id': get_by_id,
            'get_by_name': get_by_name,
            'get_by_cpf': get_by_cpf,
            'edit': edit,
            'remove': remove}
