from typing import Callable
from utils.enum_utils import ServiceException


def customer_decorator(validators: tuple) -> tuple:

    form_data_validation, id_validation = validators

    def check_data_entry(fn) -> Callable:

        def wrapper(customer: tuple) -> tuple:

            if [] != (validation_errors := form_data_validation(customer)):
                raise Exception(ServiceException.CUSTOMER,
                                {"errors": validation_errors}, 400)

            return fn(customer)

        return wrapper

    def check_parameter_id(fn) -> Callable:

        def wrapper(customer_id: int) -> tuple:

            if (validatio_error := id_validation(customer_id)):
                raise Exception(ServiceException.CUSTOMER,
                                {"error": validatio_error}, 400)

            return fn(customer_id)

        return wrapper

    return check_data_entry, check_parameter_id
