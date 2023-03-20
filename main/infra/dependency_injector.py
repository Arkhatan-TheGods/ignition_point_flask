from sqlite3 import Cursor

from main.services.customer_service import customer_service
from services.product_service import product_service

from main.infra.repositories.customer_repository import customer_repository
from infra.repositories.products_repository import products_repository

from infra.repositories.repository import repository


from decorators.customer_decorator import customer_decorator
from services.validators.customer_validator import customer_validator


def container(cursor: Cursor) -> tuple:

    customer = customer_service(customer_decorator(customer_validator()),
                                customer_repository(repository(cursor)))

    products = product_service(products_repository(repository(cursor)))

    return customer, products
