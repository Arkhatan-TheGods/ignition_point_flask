from typing import Callable
from flask import Response


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

    return {'all':all_results}