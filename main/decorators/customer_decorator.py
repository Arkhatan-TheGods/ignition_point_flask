from typing import Callable
from utils.enum_utils import TypeException


def customer_decorator(validators: tuple) -> tuple:

    input_data_validation, validation_by_id, validation_by_CPF, validation_by_name = validators

    def check_data_entry(fn) -> Callable:

        def wrapper(customer: tuple) -> tuple:

            if [] != (validation_errors := input_data_validation(customer)):
                raise Exception(TypeException.CUSTOMER,
                                {"errors": validation_errors}, 400)

            return fn(customer)

        return wrapper

    def check_id_parameter(fn) -> Callable:

        def wrapper(param: tuple) -> tuple:

            if (validatio_error := validation_by_id(param[0])):
                raise Exception(TypeException.CUSTOMER,
                                {"error": validatio_error}, 400)

            return fn(param)

        return wrapper

    def check_cpf_parameter(fn) -> Callable:

        def wrapper(param: tuple) -> tuple:

            if (validatio_error := validation_by_CPF(param[0])):
                raise Exception(TypeException.CUSTOMER,
                                {"error": validatio_error}, 400)

            return fn(param)

        return wrapper

    def check_name_parameter(fn) -> Callable:

        def wrapper(param: tuple) -> tuple:

            if (validatio_error := validation_by_name(param[0])):
                raise Exception(TypeException.CUSTOMER,
                                {"error": validatio_error}, 400)

            return fn(param)

        return wrapper

    return (check_data_entry,
            check_id_parameter,
            check_cpf_parameter,
            check_name_parameter)
