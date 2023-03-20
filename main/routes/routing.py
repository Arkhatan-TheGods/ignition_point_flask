from flask import Flask

from routes.register_customer_routes import register_customer_routes
from routes.register_product_routes import register_product_routes

from decorators.controller_decorator import controller_decorator

from controllers.customers_controller import customers_controller
from controllers.products_controller import products_controller

from services.service import get_service
from infra.dependency_injector import container


def routing(app: Flask,
            data_base: str) -> None:

    args = get_service, data_base, container

    register_customer_routes(app, customers_controller(
        controller_decorator("CUSTOMER", args)))

    register_product_routes(app, products_controller(
        controller_decorator("PRODUCT", args)))
