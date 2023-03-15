from flask import Flask

def register_product_routes(app: Flask, controller: dict) -> None:

    # app.add_url_rule('/all_costumers', 'all_results', )#container(cursor))['all'])
    app.add_url_rule('/all_costumers', controller["all"])