from typing import Callable
from flask import Flask
from costumer_services import costumer_service
from sqlite3 import Connection, Cursor, connect

from routes.costumer_route import costumer_route
# from routes.products_route import products_route

from controllers.costumer_controller import costumer_controller

from infra.repositories.repository import repository
from infra.repositories.costumer_repository import costumer_repository
from infra.repositories.products_repository import products_repository


def container(cursor: Cursor) -> tuple:

    costumer = costumer_service(costumer_repository(repository(cursor)))
    products = costumer_service(products_repository(repository(cursor)))

    return costumer, products

def injector(type_service:str) -> Callable:

    def decorator(func: Callable):
        
        def wrapper(*args, **kwargs):

            conn: Connection = connect('store.db')
        
            service: dict = {}
        
            try:

                costumer, products = container(conn.cursor())

                match type_service:
                    case 'COSTUMER':
                        service = costumer
                    case 'PRODUCTS':
                        service = products
                
                services = func(*args, **service, **kwargs)
                

            except:
                conn.rollback()
                raise

            else:

                conn.commit()

            finally:
                conn.close()

            return services
        return wrapper

    return decorator


def create_tables():

    conn: Connection | None = None

    try:
        conn = connect('store.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS CLIENTE(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            NOME TEXT NOT NULL, 
            CPF TEXT NOT NULL UNIQUE, 
            DATA_NASCIMENTO TEXT NOT NULL, 
            ENDERECO TEXT NOT NULL
            );""")

    except Exception as e:
        print(e)

    finally:
        if conn:
            conn.close()

app = Flask(__name__)

app.add_url_rule

def main(app: Flask):

    create_tables()

    costumer_route(app, costumer_controller(injector, "COSTUMER"))


if __name__ == "__main__":
    main(app)
    # comando para rodar via powershell: waitress-serve --host=127.0.0.1 --port=8080 main.app:app
    # serve(app, _quiet=True, host='127.0.0.1', port=8080, url_scheme='https', _profile=True)
    app.run(debug=True, use_reloader=False, host='127.0.0.1', port=8080)
