from flask import Flask
from waitress import serve

app = Flask(__name__)
print('nome do módulo', __name__)
# escreva as rotas aqui


@app.route('/')
def hello():
    return {'message': " Buddy."}


# aqui inicia o app e o servidor
if __name__ == "__main__":
    # comando para rodar via powershell: waitress-serve --host=127.0.0.1 --port=8080 main.app:app
    # serve(app, _quiet=True, host='127.0.0.1', port=8080, url_scheme='https', _profile=True)
    app.run(debug=True, host='127.0.0.1', port=8080)
