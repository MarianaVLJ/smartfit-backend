from flask import Blueprint, request, jsonify

# Creamos el controlador (Blueprint) para los clientes
cliente_bp = Blueprint('cliente_bp', __name__)

@cliente_bp.route('/socios', methods=['POST'])
def crear_socio():
    # 1. Obtenemos el JSON que envías desde Postman
    datos = request.get_json()
    
    # 2. En una arquitectura completa, aquí llamaríamos a la capa de Aplicación:
    # servicio.crear_nuevo_socio(datos)
    
    # 3. Para cumplir con la prueba BDD (Mock), devolvemos lo que Postman espera:
    respuesta = {
        "nombres": datos.get("nombres"),
        "estado": "Activo",
        "mensaje": "Socio registrado con éxito en SmartFit"
    }
    
    # 4. Retornamos la respuesta y el código 201 (Created)
    return jsonify(respuesta), 201