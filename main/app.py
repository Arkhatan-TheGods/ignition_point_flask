from flask import Flask

from infra.db.tables import build_tables

from routes.routing import routing

app = Flask(__name__)

build_tables('store.db')

routing(app, 'store.db')

if __name__ == "__main__":

    app.run(debug=True, use_reloader=False, host='127.0.0.1', port=8080)
