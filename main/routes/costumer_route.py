
def costumer_route(app, controller: dict) -> None:

    app.add_url_rule('/all_costumers', "all", controller["all"])
