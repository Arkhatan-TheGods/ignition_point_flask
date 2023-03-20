from flask import Flask, Request

from routes.register_customer_routes import register_customer_routes
from routes.register_product_routes import register_product_routes

from decorators.decorator import services_decorator

from controllers.customers_controller import customers_controller
from controllers.products_controller import products_controller
from infra.dependency_injector import container

def get_params(request: Request) -> dict | None:

    match request.method.upper():

        case 'POST':
            params = {"data": request.get_json()}
        case 'GET':
            params = {"id": request.args.get("id", "")}
        case 'PUT':
            params = {"id": request.args.get("id", ""),
                      "data": request.get_json()}
        case 'DELETE':
            params = {"id": request.args.get("id", "")}
        case _:
            params: dict | None = None

    return params

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

def routing(app: Flask,
            request: Request, 
            data_base: str) -> None:

    parameters = request, get_params, get_service, data_base, container

    register_customer_routes(app, customers_controller(
        services_decorator("CUSTOMER", parameters)))

    register_product_routes(app, products_controller(
        services_decorator("PRODUCT", parameters)))
