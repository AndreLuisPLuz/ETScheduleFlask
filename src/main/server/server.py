# Fazendo um servidor em Flask
from flask import Flask
from src.main.routes.routes import routes_bp

app = Flask(__name__)

app.register_blueprint(routes_bp)
#Registra as rotas relacionada a essa blueprint