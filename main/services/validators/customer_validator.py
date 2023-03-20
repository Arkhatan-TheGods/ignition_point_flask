from re import match
from datetime import datetime


def customer_validator() -> tuple:

    def validate_date(date_text: str, mask: str) -> bool:

        print(datetime.strptime(date_text, mask).strftime(mask))

        try:
            if date_text != datetime.strptime(date_text, mask).strftime(mask):
                raise ValueError
            return True
        except ValueError:
            return False

    def form_data_validation(args: tuple) -> list:

        name, cpf, birth_date, address = args

        notifications = []
        pattner_name = "^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\\s]+$"
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

    def id_validation(customer_id: int) -> str | None:

        return "Id cliente inválido" if customer_id == 0 else None

    return form_data_validation, id_validation