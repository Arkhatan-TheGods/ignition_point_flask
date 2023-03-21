
def customer_service(customer_validator: tuple, customer_repository: dict) -> dict:

    check_data_entry, check_id_parameter, check_cpf_parameter, check_name_parameter = customer_validator

    @check_data_entry
    def add(costumer: tuple) -> None:

        customer_repository['add'](costumer)

    def get_all() -> tuple:
        
        return customer_repository['all']()

    @check_id_parameter
    def get_by_id(customer_id: tuple) -> tuple:

        return customer_repository['get_by_id'](customer_id)

    @check_cpf_parameter
    def get_by_cpf(cpf: tuple) -> tuple:
        
        return customer_repository['get_by_cpf'](cpf)

    @check_name_parameter
    def get_by_name(name: tuple) -> tuple:
        
        return customer_repository['get_by_name'](name)


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
            'all': get_all,
            'get_by_id': get_by_id,
            'get_by_cpf': get_by_cpf,
            'get_by_name': get_by_name,
            'update': update}
            
