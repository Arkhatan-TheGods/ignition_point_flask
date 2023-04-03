
def customer_service(customer_validator: tuple, customer_repository: dict) -> dict:

    check_data, check_id, check_cpf, check_name = customer_validator

    @check_data
    def add(costumer: tuple) -> None:

        customer_repository['add'](costumer)

    def get_all() -> tuple:
        
        return customer_repository['all']()

    @check_id
    def get_by_id(customer_id: tuple) -> tuple:

        return customer_repository['get_by_id'](customer_id)

    @check_cpf
    def get_by_cpf(cpf: tuple) -> tuple:
        
        return customer_repository['get_by_cpf'](cpf)

    @check_name
    def get_by_name(name: tuple) -> tuple:
        
        return customer_repository['get_by_name'](name)

    # @check_data TODO: ajustar input_data_validation para que possa servir também no put
    def update_by_id(customer: tuple) -> None:
        return customer_repository['update_by_id'](customer)
        
    return {'add': add,
            'all': get_all,
            'get_by_id': get_by_id,
            'get_by_cpf': get_by_cpf,
            'get_by_name': get_by_name,
            'update_by_id': update_by_id}
            
