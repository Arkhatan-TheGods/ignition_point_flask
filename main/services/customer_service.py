
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

    #@check_data_entry
    def update_by_id(customer: tuple) -> None:
        return customer_repository['update_by_id'](customer)
        
    return {'add': add,
            'all': get_all,
            'get_by_id': get_by_id,
            'get_by_cpf': get_by_cpf,
            'get_by_name': get_by_name,
            'update_by_id': update_by_id}
            
