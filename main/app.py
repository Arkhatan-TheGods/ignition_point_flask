from flask import Flask, jsonify, Response
from waitress import serve
from costumer_services import costumer_service
import db_operation as operation
from traceback import print_exc
import adapter_repository as adapter
from sqlite3 import Connection, Cursor
from controllers.costumer_controller import costumer_controller


def container(cursor: Cursor):
    # costumer = costumer_service(adapter.costumer(operation.operator(cursor)))

    pass


print('chegando aqui<<<<<<<<<<<<<<<<<<<<<<')
app = Flask(__name__)
# print('nome do módulo', __name__)
# escreva as rotas aqui


def routing(app):

    @app.route('/')
    def hello():
        operation.create_table_costumer()
        return {'message': "Hello Buddy"}

    conn = operation.connect_to_db()
    cursor = conn.cursor()
    app.add_url_rule('/all_costumers', 'all_results', costumer_controller)#container(cursor))['all'])
    # @app.route('/all_costumers', methods=['GET'])
    conn.close()


# aqui inicia o app e o servidor
if __name__ == "__main__":
    routing(app)
    # comando para rodar via powershell: waitress-serve --host=127.0.0.1 --port=8080 main.app:app
    # serve(app, _quiet=True, host='127.0.0.1', port=8080, url_scheme='https', _profile=True)
    app.run(debug=True, host='127.0.0.1', port=8080)

