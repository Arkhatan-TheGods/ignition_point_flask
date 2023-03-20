from typing import Callable
from flask import request

def customers_controller(services: Callable) -> dict:

    @services
    def create(**kwargs) -> dict:

        if request.headers['Content-Type'] != 'application/json':
            raise Exception({"message": 'Header Error', "status_code": 415})

        customer = tuple(request.get_json())

        print("customer:", customer)

        # customer = tuple(args[0]["data"].values())

        # kwargs["services"]["add"](customer)

        return {"data": "Cliente cadastrado com sucesso", "status_code": 200}

    @services
    def get_customer(**kwargs) -> dict:

        customers = kwargs["services"]["all"]()

        print("customer_controller.get_customer.costumers:_", customers)

        return {"data": customers, "status_code": 200}

    return {'create': create,
            'all': get_customer}
