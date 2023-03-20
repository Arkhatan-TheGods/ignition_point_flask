def get_service(container: tuple, type_service: str) -> dict | None:

    costumer, products = container

    match type_service:
        case 'COSTUMER':
            service = costumer
        case 'PRODUCTS':
            service = products
        case _:
            service: dict | None = {}

    return service
