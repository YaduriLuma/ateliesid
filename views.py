from flask import render_template, request, make_response, session


def init_app(app):
    @app.route("/", methods=['POST', 'GET'])
    def index():
        titulo = 'Index'
        products = ['um', 'dois', 'tres', 'quatro']
        context = dict(titulo=titulo, products=products)
        return render_template('index.html', **context)

    @app.route("/login", methods=['POST', 'GET'])
    def login():
        title = 'Login'
        error = ''
        if request.method == 'POST':
            return render_template('index.html', error=error)
        else:
            error = 'Usuário ou senha incorretos'
        context = dict(title=title, error=error)
        return render_template('login.html', **context)

    @app.route("/usuarios/<nome_usuario>")
    def usuarios(nome_usuario):
        return render_template('usuarios.html', nome_usuario=nome_usuario)


