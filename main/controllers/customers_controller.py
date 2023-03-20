from typing import Callable

def customers_controller(services: Callable) -> dict:

    @services
    def create(*args, **kwargs) -> dict:

        customer = tuple(args[0]["data"].values())

        row_id = kwargs["services"]["add"](customer)

        print("customer_controller.create.row_id:_", row_id)

        return {"data": "Cliente cadastrado com sucesso", "status_code": 200}

    @services
    def get_customer(**kwargs) -> dict:

        customers = kwargs["services"]["all"]()

        print("customer_controller.get_customer.costumers:_", customers)

        return {"data": customers, "status_code": 200}

    return {'create': create,
            'all': get_customer}
