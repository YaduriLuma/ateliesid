import functools

from flask import render_template, request, make_response, session, redirect, url_for, g, Blueprint
from models.User import User
from models.Product import Product, Type, producttypes
from ext import commands
from werkzeug.security import check_password_hash, generate_password_hash

global logado
logado = False
global produtos
produtos = Product
global tipos
tipos = Type
global tipos_produtos
tipos_produtos = producttypes

bp = Blueprint('', __name__, url_prefix='/')


@bp.route("/", methods=['POST', 'GET'])
def index():
    title = 'Index'
    if 'email' in session:
        title = session['email']
    products = ['um', 'dois', 'tres', 'quatro']
    global tipos
    tipos = Type.query.all()
    context = dict(title=title, products=products, logado=logado, types=tipos)
    return render_template('index.html', **context)


@bp.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    title = 'Login'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user is None:
            error = 'Usuário incorreto.'
        elif not check_password_hash(user.password, password):
            error = 'Senha incorreta.'
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index'))
    context = dict(title=title, error=error)
    return render_template('login.html', **context)


@bp.before_app_request
def load_logged_in_user():
    """user_id = session.get('user_id')"""
    user_id = None
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view


@bp.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)


@bp.route("/resetdb")
def resetdb():
    commands.drop_db()
    commands.create_db()
    commands.populate_db()
    return redirect(url_for('index'))
