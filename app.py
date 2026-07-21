from flask import Flask
from src.presentation.controllers.cliente_controller import cliente_bp

app = Flask(__name__)

# Registramos el controlador de la capa de presentación
app.register_blueprint(cliente_bp)

if __name__ == '__main__':
    # Arrancamos el servidor en el puerto 5000
    app.run(debug=True, port=5000)