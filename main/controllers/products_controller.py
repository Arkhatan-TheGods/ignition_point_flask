from typing import Callable


def products_controller(services: Callable):

    @services
    def add(*args, **kwargs):

        services = kwargs

        # costumers = services["add"]()

        return {"product": []}

    return {'add': add}
