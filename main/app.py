from flask import Flask, jsonify, Response
from waitress import serve
from costumer_services import costumer_service
import db_operation as operation
from traceback import print_exc
import adapter_repository as adapter
from sqlite3 import Connection, Cursor


def container(cursor: Cursor) -> dict:
    costumer = costumer_service(adapter.costumer(operation.operator(cursor)))

    return costumer


app = Flask(__name__)
# print('nome do módulo', __name__)
# escreva as rotas aqui


@app.route('/')
def hello():
    operation.create_table_costumer()
    return {'message': "Hello Buddy"}

app.add_url_rule('/all_costumers', 'all_results', all_results)
#@app.route('/all_costumers', methods=['GET'])



# aqui inicia o app e o servidor
if __name__ == "__main__":
    # comando para rodar via powershell: waitress-serve --host=127.0.0.1 --port=8080 main.app:app
    # serve(app, _quiet=True, host='127.0.0.1', port=8080, url_scheme='https', _profile=True)
    app.run(debug=True, host='127.0.0.1', port=8080)
