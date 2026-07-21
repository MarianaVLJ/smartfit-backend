from flask import Blueprint, request, jsonify
from src.application.services.suscripcion_service import SuscripcionService

suscripcion_bp = Blueprint("suscripcion_bp", __name__)

service = SuscripcionService()


@suscripcion_bp.route("/suscripciones", methods=["POST"])
def crear_suscripcion():

    datos = request.get_json()

    resultado = service.crear_suscripcion(datos)

    return jsonify({
        "mensaje": "Suscripción registrada correctamente",
        "suscripcion": resultado
    }), 201


@suscripcion_bp.route("/suscripciones", methods=["GET"])
def listar():

    return jsonify(service.listar_suscripciones()), 200


@suscripcion_bp.route("/contingencia", methods=["POST"])
def crear_contingencia():

    datos = request.get_json()

    resultado = service.registrar_contingencia(datos)

    return jsonify({
        "mensaje": "Acceso contingencial registrado",
        "contingencia": resultado
    }), 201


@suscripcion_bp.route("/contingencia", methods=["GET"])
def listar_contingencia():

    return jsonify(service.listar_contingencias()), 200