from flask import Flask


def register_customer_routes(app: Flask, controller: dict) -> None:

    app.add_url_rule('/customers/', "create_customers", controller["create"], methods=['POST'])

    app.add_url_rule('/customers/', "get_customers", controller["all"], methods=['GET'])

    app.add_url_rule('/customers/<int:customer_id>', "get_customer_by_id", controller["get_by_id"], methods=['GET'])

    app.add_url_rule('/customers/<string:cpf>', "get_customer_by_cpf", controller["get_by_cpf"], methods=['GET'])

    app.add_url_rule('/customers/<string:name>/name', "get_customer_by_name",
                     controller["get_by_name"], methods=['GET'])

    app.add_url_rule('/customers/<int:customer_id>', "edit_customer", controller["update_by_id"], methods=['PUT'])

    app.add_url_rule('/customers/<int:customer_id>', "delete_customer", controller["delete_by_id"], methods=['DELETE'])
