from typing import Callable


def costumer_controller(service: Callable):

    @service
    def all_results(*args, **kwargs):

        # print("kwargs:", kwargs)
        
        services = kwargs

        costumers = services["all"]()

        return {"costumers": costumers}

    return {'all': all_results}


# @my_decorator
# def costumer_controller(services: Callable) -> dict:
#     def all_results() -> Response:
#         results = []
#         try:

#             results = services['all']()
#         except Exception as e:
#             print('error>>>>>>>>>>>>', e)
#             print_exc()
#         finally:
#             # conn.close()
#             return jsonify(results) if results else {'results': 'none'}

#     return {'all': all_results}
