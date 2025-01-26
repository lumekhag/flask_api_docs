
from flask import Blueprint, render_template

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home():
    """
    Renderiza a página inicial.

    Esta função está associada à URL raiz (`/`) da aplicação e renderiza o
    template `index.html`.

    :return: Template HTML renderizado para a página inicial.
    :rtype: flask.Response
    """
    return render_template('index.html')
