from typing import Callable


def costumer_controller(services: Callable, name: str):

    @services(name)
    def all_results(*args, **kwargs):

        services = kwargs

        costumers = services["all"]()

        return {"costumers": costumers}

    return {'all': all_results}
