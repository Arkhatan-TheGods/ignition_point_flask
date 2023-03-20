from typing import Callable


def customer_decorator(validators: tuple) -> tuple:

    form_data_validation, id_validation = validators

    def check_data_entry(fn) -> Callable:

        def wrapper(customer: tuple) -> tuple:

            if [] != (notifications := form_data_validation(customer)):
                raise Exception(
                    {"notifications": notifications, "status_code": 400})

            return fn(customer)

        return wrapper

    def check_parameter_id(fn) -> Callable:

        def wrapper(customer_id: int) -> tuple:

            if (notify := id_validation(customer_id)):
                raise Exception(
                    {"notify": notify, "status_code": 400})

            return fn(customer_id)

        return wrapper

    return check_data_entry, check_parameter_id
