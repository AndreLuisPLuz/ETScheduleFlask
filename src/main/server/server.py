from flask import Flask
from src.main.routes.graphs_routes import  graphs_routes_bp

app = Flask(__name__)

app.register_blueprint(graphs_routes_bp)