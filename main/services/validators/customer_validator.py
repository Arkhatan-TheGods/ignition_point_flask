from typing import Callable
from re import match
from datetime import datetime


def costumer_validator() -> tuple:

    def validate_date(date_text: str, mask: str) -> bool:

        print(datetime.strptime(date_text, mask).strftime(mask))

        try:
            if date_text != datetime.strptime(date_text, mask).strftime(mask):
                raise ValueError
            return True
        except ValueError:
            return False

    def check_data(args: tuple) -> list:

        name, cpf, birth_date, address = args

        notifications = []
        pattner_name = '^[a-zA-Z0-9\\s]+$'
        pattner_cpf = "\\d{3}\\.\\d{3}(\\.\\d{3}\\-\\d{2})"

        print(match(pattner_cpf, cpf))

        if len(name) < 1:
            notifications.append("Campo name não informado")
        else:
            if match(pattner_name, name) is None:
                notifications.append("Campo nome inválido")

        if match(pattner_cpf, cpf) is None:
            notifications.append("Formato inválido para campo cpf")

        if len(birth_date) < 1:
            notifications.append("Campo data de nascimento não informado")
        else:
            if validate_date(birth_date, "%d/%m/%Y") is False:
                notifications.append("Campo data de nascimento inválido")

        if len(address) < 1:
            notifications.append("Campo endereço não informado")

        return notifications

    def check_id():
        return "check_id"

    return check_data, check_id


def check_costomer_decorator(validators: dict) -> dict:

    def check_create(func) -> Callable:
        def wrapper() -> tuple:

            if len(notifys := validators["check_data"]()) >= 1:
                raise Exception({"notifys": notifys, "status_code": 403})

            return func(func)
        return wrapper

    def check_parameter(func) -> Callable:
        def wrapper() -> tuple:

            if len(notifys := validators["check_id"]()) >= 1:
                raise Exception(notifys)

            return func(func)
        return wrapper

    return {"check_create": check_create,
            "check_parameter": check_parameter}
