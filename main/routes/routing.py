from flask import Flask

from routes.register_customer_routes import register_customer_routes
from routes.register_product_routes import register_product_routes

from decorators.decorator import services_decorator

from controllers.customers_controller import customers_controller
from controllers.products_controller import products_controller

from services.service import get_service
from infra.dependency_injector import container

# def parameters_routes():

#     def customer_parameters(request: Request) -> dict | None:

#         match request.method.upper():

#             case 'POST':
#                 params = {"data": request.get_json()}
            
#             case 'GET':
#                 params = {"id": request.args.get("id", "")}
            
#             case 'PUT':
#                 params = {"id": request.args.get("id", ""),
#                         "data": request.get_json()}
#             case 'DELETE':
#                 params = {"id": request.args.get("id", "")}
#             case _:
#                 params: dict | None = None

#         return params
    
#     return customer_parameters



# def get_parameters(request: Request) -> dict | None:

#     match request.method.upper():

#         case 'POST':
#             params = {"data": request.get_json()}
        
#         case 'GET':
#             params = {"id": request.args.get("id", "")}
        
#         case 'PUT':
#             params = {"id": request.args.get("id", ""),
#                       "data": request.get_json()}
#         case 'DELETE':
#             params = {"id": request.args.get("id", "")}
#         case _:
#             params: dict | None = None

#     return params


# def routing(app: Flask,
#             request: Request,
#             data_base: str) -> None:

    # args = request, get_parameters, get_service, data_base, container

def routing(app: Flask,
            data_base: str) -> None:

    args = get_service, data_base, container

    register_customer_routes(app, customers_controller(
        services_decorator("CUSTOMER", args)))

    register_product_routes(app, products_controller(
        services_decorator("PRODUCT", args)))
