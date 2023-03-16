from flask import Flask
from routes.routing import routing
from infra.db.db_context import Connection, execute_connect
from infra.db.create_tables import create_tables
from infra.db.query_tables import query_tables
from config import get_config
from traceback import format_exc


conn: Connection | None = None
try:
    config = get_config()

    data_base = config.get('file_db')

    if data_base is None:
        raise Exception(
            "Data base não identificado, verificar arquivo settings.yaml")

    conn = execute_connect(data_base)

    create_tables(conn, query_tables())

except Exception:
    # TODO: Criar funcionalidade para armazenar log de erros
    print(format_exc())
else:

    app = Flask(__name__)

    routing(app, data_base)

    if __name__ == "__main__":

        app.run(debug=True, use_reloader=False, host='127.0.0.1', port=8080)

finally:
    if conn:
        conn.close()
        print()
