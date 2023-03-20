from sqlite3 import Cursor

from main.services.customer_service import customer_service
from services.product_service import product_service

from infra.repositories.costumer_repository import costumer_repository
from infra.repositories.products_repository import products_repository

from infra.repositories.repository import repository


def container(cursor: Cursor) -> tuple:

    costumer = customer_service(costumer_repository(repository(cursor)))
    products = product_service(products_repository(repository(cursor)))

    return costumer, products
