from flask import Flask
from src.infrastructure.database import db
from src.presentation.controllers.cliente_controller import cliente_bp

app = Flask(__name__)

# Configuración de la base de datos SQLite local para el laboratorio
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartfit.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy con la app
db.init_app(app)

# Registrar el Blueprint del módulo de clientes
app.register_blueprint(cliente_bp)

# Crear las tablas automáticamente al iniciar
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5000)