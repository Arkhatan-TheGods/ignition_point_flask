
def costumer_service(costumer_repository: dict) -> dict:

    def add(costumer: tuple) -> None:

        row_id = costumer_repository['add'](costumer)

        print("costumer_service.add.row_id:_", row_id)

    def get_by_cpf() -> str:

        cpf = costumer_repository['all']()

        print("costumer_service.get_by_cpf.result:_", cpf)

        return

    def get_all() -> list[tuple]:

        result = costumer_repository['all']()

        print("costumer_service.get_all.result:_", result)

        return []

    def update(costumer, ID: int) -> None:
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
            'update': update,
            'all': get_all}
