from flask import Flask

from routes.routing import routing

from infra.db.db_context import execute_connect
from infra.db.setup_tables import setup_tables
from infra.db.query_tables import query_tables

app = Flask(__name__)

if setup_tables(execute_connect('store.db'), query_tables()):
    routing(app, 'store.db')

if __name__ == "__main__":

    app.run(debug=True, use_reloader=False, host='127.0.0.1', port=8080)
