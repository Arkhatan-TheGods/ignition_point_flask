def products_route(app, controller) -> None:

    # app.add_url_rule('/all_costumers', 'all_results', )#container(cursor))['all'])
    app.add_url_rule('/all_costumers', controller["all"])