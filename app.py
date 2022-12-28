from flask import Flask, render_template, request, make_response, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/oi/')
@app.route('/oi/<nome>')
def oi(nome=None):
    return render_template('oi.html', nome=nome)


@app.route("/")
def index():
    username = request.cookies.get('username')
    resp = make_response(render_template('index.html'))
    if username is None:
        username = ''
    resp.set_cookie('username', username)
    return resp


@app.route("/login")
def login():
    error = None
    if request.method == 'POST':
        return render_template('index.html')
    else:
        error = 'Usuário ou senha incorretps'
    return render_template('index.html', error=error)


@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)


if __name__ == "__main__":
    app.run(debug=True)

