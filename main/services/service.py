def get_service(container: tuple, type_service: str) -> dict | None:

    customer, products = container

    match type_service:
        case 'CUSTOMER':
            service = customer
        case 'PRODUCTS':
            service = products
        case _:
            service: dict | None = {}

    return service
