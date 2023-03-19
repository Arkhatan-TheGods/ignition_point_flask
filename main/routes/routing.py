from typing import Callable
from flask import Flask, Request

from routes.register_customer_routes import register_customer_routes
from routes.register_product_routes import register_product_routes

from decorators.decorator import services_decorator
from controllers.costumers_controller import costumer_controller
from controllers.products_controller import products_controller

def routing(app: Flask, 
            request: Request, 
            check_params:Callable, 
            get_service:Callable, 
            data_base: str) -> None:

    register_customer_routes(app, costumer_controller(
        services_decorator(request, check_params, get_service, data_base, "COSTUMER")))

    register_product_routes(app, products_controller(
        services_decorator(request, check_params, get_service, data_base, "PRODUCT")))
