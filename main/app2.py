from flask import Flask, jsonify, Response
from costumer_services import costumer_service as service
import db_operation as operation
from traceback import print_exc
import adapter_repository as adapter
from sqlite3 import Connection, Cursor
from controllers.costumer_controller import costumer_controller


operation.create_table_costumer()

def all_info() -> jsonify:
    conn = operation.connect_to_db()
    cursor = conn.cursor()
    results = cursor.execute('select * from CLIENTE;').fetchall()
    print(results)
    conn.close()
    return jsonify(results)


app = Flask(__name__)

@app.route('/')
def home() -> str:
    return 'Hello, buddy!'

conn = operation.connect_to_db()
cursor = conn.cursor()

@app.route('/costumers')
def all(cursor) -> jsonify:
    results = cursor.execute('select * from cliente;').fetchall()
    return jsonify(results)

all(cursor)
conn.close()
# app.add_url_rule('/costumers', 'costumers', all_info, methods=['GET'])



if __name__ == '__main__':
    app.run(debug=True)