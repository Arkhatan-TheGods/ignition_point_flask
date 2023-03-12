from flask import Flask, jsonify
from waitress import serve
from costumer_services import costumer_service
import db_operation as operation
from traceback import print_exc


app = Flask(__name__)
# print('nome do módulo', __name__)
# escreva as rotas aqui


@app.route('/')
def hello():
    operation.create_table_costumer()
    return {'message': "Hello Buddy"}


@app.route('/all_costumers')
def all_results():
    try:

        conn = operation.connect_to_db()

    except Exception as e:
        print(e)
        print_exc()
    else:
        fn = costumer_service(conn)
        results = fn['all']()

    finally:
        conn.close()
        return jsonify(results) if results else {'results': 'none'}


# aqui inicia o app e o servidor
if __name__ == "__main__":
    # comando para rodar via powershell: waitress-serve --host=127.0.0.1 --port=8080 main.app:app
    # serve(app, _quiet=True, host='127.0.0.1', port=8080, url_scheme='https', _profile=True)
    app.run(debug=True, host='127.0.0.1', port=8080)
