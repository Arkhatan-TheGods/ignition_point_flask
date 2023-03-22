from re import match
from datetime import datetime


def customer_validator() -> tuple:

    PATTERN_CPF = "\\d{3}\\.\\d{3}(\\.\\d{3}\\-\\d{2})"
    PATTERN_NAME = "^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\\s]+$"

    def validate_date(date_text: str, mask: str) -> bool:

        print(datetime.strptime(date_text, mask).strftime(mask))

        try:
            if date_text != datetime.strptime(date_text, mask).strftime(mask):
                raise ValueError
            return True
        except ValueError:
            return False

    def input_data_validation(data: tuple) -> list:

        name, cpf, birth_date, address = data

        notifications = []

        if len(name) < 1:
            notifications.append("Campo nome não informado")
        else:
            if match(PATTERN_NAME, name) is None:
                notifications.append("Campo nome inválido")

        if len(cpf) < 1:
            notifications.append("Campo cpf não informado")

        if match(PATTERN_CPF, cpf) is None:
            notifications.append("Formato inválido para campo cpf")

        if len(birth_date) < 1:
            notifications.append("Campo data de nascimento não informado")
        else:
            if validate_date(birth_date, "%d/%m/%Y") is False:
                notifications.append("Campo data de nascimento inválido")

        if len(address) < 1:
            notifications.append("Campo endereço não informado")

        return notifications

    def validation_by_id(param_id: int) -> str | None:

        return "Id inválido" if param_id == 0 else None

    def validation_by_CPF(cpf: str) -> str | None:
        return "Formato inválido para campo cpf" \
            if match(PATTERN_CPF, cpf) is None else None

    def validation_by_name(name: str) -> list:

        notifications = []

        if len(name.strip()) < 3:
            notifications.append("Campo nome deve possuir mínimo de 3 caracteres")
        else:
            if match(PATTERN_NAME, name) is None:
                notifications.append("Campo nome inválido")

        return notifications

    return (input_data_validation, 
            validation_by_id, 
            validation_by_CPF, 
            validation_by_name)
