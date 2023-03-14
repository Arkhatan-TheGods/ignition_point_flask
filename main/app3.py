from flask import Flask

from infra.db.tables import build_tables

from routes.costumer_route import costumer_route

from decorators.decorator import decorator

from controllers.costumer_controller import costumer_controller

app = Flask(__name__)

app.add_url_rule

build_tables('store.db')

costumer_route(app, costumer_controller(decorator('store.db'), "COSTUMER"))

if __name__ == "__main__":

    app.run(debug=True, use_reloader=False, host='127.0.0.1', port=8080)
