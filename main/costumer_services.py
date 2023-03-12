from time import sleep
from typing import Callable


def costumer_service(repository: Callable) -> dict:

    def add() -> tuple:
        name = input('Nome: ').strip()
        cpf = input('CPF:').strip()
        data_nascimento = input('data de nascimento (DD/MM/AAAA): ').strip()
        endereco = input('Endereço: ').strip()
        return (name, cpf, data_nascimento, endereco)

    def update(costumer, ID: int) -> tuple:

        result = costumer['get_costumer_by_id'](ID)

        values_dict = {
            'nome': result[1],
            'cpf': result[2],
            'data_nascimento': result[3],
            'endereço': result[4], }

        print(result, '\n dê enter para manter os valores atuais.')
        for key in values_dict:
            novo_valor = input(f"novo valor para {c}: ").strip()
            if novo_valor != "":
                dados[key] = novo_valor

        return (values_dict['nome'],
                values_dict['cpf'],
                values_dict['data_nascimento'],
                values_dict['endereço'], ID)

    # def get_all() -> list[tuple]:
    #     if conn is None:
    #         raise Exception('falha de conexão com o banco de dados')
    #         # conn = operation.connect_to_db()

    #     costumers = []
    #     cursor = conn.cursor()
    #     costumer = adapter.costumer(operation.operator(cursor))
    #     results = costumer['show_all']()
    #     for v in results:
    #         costumers.append(v)
    #         sleep(0.2)

    #     return costumers

    def get_all() -> list[tuple]:
        return repository['all']()

    return {'add': add,
            'update': update,
            'all': get_all, }
