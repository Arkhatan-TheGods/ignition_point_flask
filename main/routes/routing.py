from typing import Callable
from flask import Flask, Request

from routes.register_customer_routes import register_customer_routes
from routes.register_product_routes import register_product_routes

from decorators.decorator import services_decorator

from controllers.customers_controller import customers_controller
from controllers.products_controller import products_controller



def routing(app: Flask,
            request: Request, 
            get_params:Callable, 
            get_service:Callable, 
            data_base: str) -> None:

    register_customer_routes(app, customers_controller(
        services_decorator(request,
                           get_params,
                           get_service,
                           data_base,
                           "CUSTOMER")))

    register_product_routes(app, products_controller(
        services_decorator(request, get_params, get_service, data_base, "PRODUCT")))
