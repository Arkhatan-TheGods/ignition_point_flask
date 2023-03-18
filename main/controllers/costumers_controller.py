from typing import Callable


def costumer_controller(services: Callable):

    @services
    def create(*args, **kwargs) -> dict:

        costumer = tuple(args[0]["data"].values())

        row_id = kwargs["services"]["add"](costumer)

        print("costumer_controller.create.row_id:_", row_id)

        return {"data": "Cliente cadastrado com sucesso", "status_code": 200}

    @services
    def get_costumer(**kwargs) -> dict:

        costumers = kwargs["services"]["all"]()

        print("costumer_controller.get_costumer.costumers:_", costumers)

        return {"data": costumers, "status_code": 200}

    return {'create': create,
            'all': get_costumer}
