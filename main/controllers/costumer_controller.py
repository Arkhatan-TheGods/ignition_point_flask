from typing import Callable
from flask import Response

# goto: implementar decorador para IoC


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def costumer_controller(services: Callable) -> dict:
    def all_results() -> Response:
        results = []
        try:

            results = services['all']()
        except Exception as e:
            print('error>>>>>>>>>>>>', e)
            print_exc()
        finally:
            # conn.close()
            return jsonify(results) if results else {'results': 'none'}

    return {'all': all_results}
