from typing import Callable
from flask import request


def customers_controller(controller: Callable) -> dict:

    @controller
    def create(services: dict) -> tuple:

        if request.headers['Content-Type'] != 'application/json':
            raise Exception('Header Error', 415)

        customer = tuple(request.get_json().values())

        services["add"](customer)

        return "Cliente cadastrado com sucesso", 200

    @controller
    def get_customer(services: dict) -> tuple:

        customers = services["all"]()

        return customers, 200

    return {'create': create,
            'all': get_customer}
