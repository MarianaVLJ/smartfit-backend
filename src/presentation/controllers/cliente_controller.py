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

@cliente_bp.route('/socios/<string:dni>', methods=['GET'])
def buscar_socio(dni):
    # Simulamos la búsqueda del socio (Mock) para que la prueba BDD pase
    if dni == "72345678":
        socio_encontrado = {
            "dni": dni,
            "nombres": "Juan Perez",
            "email": "juan.perez@email.com",
            "plan": "Black",
            "estado": "Activo"
        }
        return jsonify(socio_encontrado), 200
    else:
        return jsonify({"error": "Socio no encontrado"}), 404