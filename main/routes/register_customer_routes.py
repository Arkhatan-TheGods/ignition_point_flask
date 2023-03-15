from flask import Flask


def register_customer_routes(app: Flask, controller: dict) -> None:

    app.add_url_rule('/costumers', "create_costumer",
                     controller["add"], methods=['POST'])

    app.add_url_rule('/costumers', "get_costumers",
                     controller["all"], methods=['GET'])
