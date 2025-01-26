
from flask import Flask
from routes.main import main_blueprint

app = Flask(__name__)

# Registrar Blueprints
app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    """
    Inicializa e executa a aplicação Flask.

    Este módulo configura a aplicação Flask, regista o blueprint principal 
    e a executa no modo de depuração.

    :return: Nenhum valor é retornado diretamente, mas a aplicação Flask é iniciada.
    """
    app.run(debug=True)

