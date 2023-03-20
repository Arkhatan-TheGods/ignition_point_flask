
def customer_service(customer_validator: tuple, customer_repository: dict) -> dict:

    check_data_entry, check_paramter = customer_validator

    @check_data_entry
    def add(costumer: tuple) -> None:

        row_id = customer_repository['add'](costumer)

        print("customer_service.add.row_id:_", row_id)

    @check_paramter
    def get_by_cpf() -> tuple:

        cpf = customer_repository['get_by_cpf']()

        print("customer_service.get_by_cpf.result:_", cpf)

        return cpf,

    def get_all() -> list[tuple]:

        result = customer_repository['all']()

        print("customer_service.get_all.result:_", result)

        return []

    @check_data_entry
    def update(customer, id: int) -> None:
        pass
        # result = costumer['get_costumer_by_id'](ID)

        # values_dict = {
        #     'nome': result[1],
        #     'cpf': result[2],
        #     'data_nascimento': result[3],
        #     'endereço': result[4], }

        # print(result, '\n dê enter para manter os valores atuais.')
        # for key in values_dict:
        #     novo_valor = input(f"novo valor para {c}: ").strip()
        #     if novo_valor != "":
        #         dados[key] = novo_valor

        # return (values_dict['nome'],
        #         values_dict['cpf'],
        #         values_dict['data_nascimento'],
        #         values_dict['endereço'], ID)

    return {'add': add,
            'get_by_cpf': get_by_cpf,
            'update': update,
            'all': get_all}
