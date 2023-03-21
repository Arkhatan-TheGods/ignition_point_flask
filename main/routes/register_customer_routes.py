from flask import Flask

def register_customer_routes(app: Flask, controller: dict) -> None:

    app.add_url_rule('/customers/', "create_customers", controller["create"], methods=['POST'])

    app.add_url_rule('/customers/', "get_customers", controller["all"], methods=['GET'])

    app.add_url_rule('/customers/<int:customer_id>', "get_customer_by_id", controller["get_by_id"], methods=['GET'])

    # /account/[account_id]/campaigns/[campaign_id]/edit

    app.add_url_rule('/customers/<string:cpf>', "get_customer_by_cpf", controller["get_by_cpf"], methods=['GET'])

    # POST http://127.0.0.1:8080/costumers        
   
    # GET http://127.0.0.1:8080/costumers/<int:id>

    # GET http://127.0.0.1:8080/costumers
        
    # PUT http://127.0.0.1:8080/costumers/<int:id>

    # DELETE http://127.0.0.1:8080/costumers/<int:id>
