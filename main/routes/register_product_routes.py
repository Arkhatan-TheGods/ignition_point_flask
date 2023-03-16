from flask import Flask

def register_product_routes(app: Flask, controller: dict) -> None:

    app.add_url_rule('/products', "create_products", controller["add"], methods=['POST'])
