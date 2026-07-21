from flask import Blueprint, request, jsonify
from src.application.services.socio_service import SocioService

cliente_bp = Blueprint('cliente_bp', __name__)
servicio = SocioService()

@cliente_bp.route('/socios', methods=['POST'])
def crear_socio():
    datos = request.get_json()
    resultado = servicio.registrar_socio(datos)
    return jsonify({
        "estado": resultado["estado"],
        "mensaje": "Socio registrado con éxito en SmartFit",
        "nombres": resultado["nombres"]
    }), 201

@cliente_bp.route('/socios/<string:dni>', methods=['GET'])
def buscar_socio(dni):
    resultado = servicio.obtener_socio(dni)
    if resultado:
        return jsonify(resultado), 200
    return jsonify({"error": "Socio no encontrado"}), 404

@cliente_bp.route('/socios/<string:dni>', methods=['PUT'])
def actualizar_socio(dni):
    datos = request.get_json()
    resultado = servicio.modificar_socio(dni, datos)
    if resultado:
        return jsonify({
            "dni": resultado["dni"],
            "nombres": resultado["nombres"],
            "plan": resultado["plan"],
            "estado": resultado["estado"],
            "mensaje": "Socio actualizado con éxito"
        }), 200
    return jsonify({"error": "Socio no encontrado"}), 404

@cliente_bp.route('/socios/<string:dni>', methods=['DELETE'])
def eliminar_socio(dni):
    exito = servicio.dar_de_baja_socio(dni)
    if exito:
        return jsonify({
            "dni": dni,
            "mensaje": "Socio eliminado con éxito"
        }), 200
    return jsonify({"error": "Socio no encontrado"}), 404