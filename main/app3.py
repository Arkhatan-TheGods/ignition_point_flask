from flask import Flask, jsonify, Response
from waitress import serve
from costumer_services import costumer_service
import db_operation as operation
from traceback import print_exc
import adapter_repository as adapter
from sqlite3 import Connection, Cursor, connect

from routes.costumer_route import costumer_route
from routes.products_route import products_route

from controllers.costumer_controller import costumer_controller
from controllers.products_controller import products_controller



def container(cursor: Cursor) -> tuple:

    costumer = costumer_service(adapter.costumer(operation.operator(cursor)))
    products = costumer_service(adapter.costumer(operation.operator(cursor)))

    return costumer, products

# def container_dependence_injection(func):

#     def wrapper(*args, **kwargs):

#         print("Something is happening before the function is called.")

#         container()

#         func(*args, **kwargs)
#         # response = func(*args, **kwargs)

#         # print(response)

#         print("Something is happening after the function is called.")

#     return wrapper

def injector(func):

    def wrapper(*args, **kwargs):
        
        conn = connect('store.db')

        try:

            cursor = conn.cursor()

            costumer, products = container(cursor)
            
            result = func(*args, **costumer, **kwargs)

        except:
            conn.rollback()
            print("SQL failed")
            raise
    
        else:
            conn.commit()
    
        finally:
            conn.close()
    
        return result
    
    return wrapper

app = Flask(__name__)

def main(app: Flask):

    costumer_route(app, costumer_controller(injector))


if __name__ == "__main__":
    main(app)
    # comando para rodar via powershell: waitress-serve --host=127.0.0.1 --port=8080 main.app:app
    # serve(app, _quiet=True, host='127.0.0.1', port=8080, url_scheme='https', _profile=True)
    app.run(debug=True, use_reloader=False, host='127.0.0.1', port=8080)
