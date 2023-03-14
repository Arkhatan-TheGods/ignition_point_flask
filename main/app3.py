from flask import Flask
from sqlite3 import Connection, connect



from routes.costumer_route import costumer_route

from decorators.decorator import decorator
# from routes.products_route import products_route

from controllers.costumer_controller import costumer_controller

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

    costumer_route(app, costumer_controller(decorator(), "COSTUMER"))


if __name__ == "__main__":
    main(app)
    # comando para rodar via powershell: waitress-serve --host=127.0.0.1 --port=8080 main.app:app
    # serve(app, _quiet=True, host='127.0.0.1', port=8080, url_scheme='https', _profile=True)
    app.run(debug=True, use_reloader=False, host='127.0.0.1', port=8080)
