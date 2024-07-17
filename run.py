from datetime import timedelta
from src.main.server.server import app
from src.models.settings.db_connection_handler import db_connection_handler
from flask_jwt_extended import JWTManager
import string, random


if __name__ == "__main__":
    db_connection_handler.connect()
    randon_str = string.ascii_letters + string.digits + string. ascii_uppercase
    
    app.config['SECRET_KEY'] = ''.join(random.choice(randon_str) for i in range(12))
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours = 1)  # Expira em 1 hora
    
    jwt = JWTManager(app)

    app.run(host="0.0.0.0", port=3000, debug=True)
    