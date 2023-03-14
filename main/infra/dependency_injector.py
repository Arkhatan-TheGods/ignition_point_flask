from sqlite3 import Cursor

from costumer_services import costumer_service

from infra.repositories.costumer_repository import costumer_repository
from infra.repositories.products_repository import products_repository

from infra.repositories.repository import repository

def container(cursor: Cursor) -> tuple:

    costumer = costumer_service(costumer_repository(repository(cursor)))
    products = costumer_service(products_repository(repository(cursor)))

    return costumer, products

