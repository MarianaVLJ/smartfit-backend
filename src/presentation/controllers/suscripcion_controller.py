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
        "suscripcion": {
            "id": resultado.id,
            "dni": resultado.dni,
            "plan": resultado.plan,
            "fecha_inicio": resultado.fecha_inicio
        }
    }), 201



@suscripcion_bp.route("/suscripciones", methods=["GET"])
def listar():

    suscripciones = service.listar_suscripciones()

    lista = []

    for suscripcion in suscripciones:
        lista.append({
            "id": suscripcion.id,
            "dni": suscripcion.dni,
            "plan": suscripcion.plan,
            "fecha_inicio": suscripcion.fecha_inicio
        })

    return jsonify(lista), 200



@suscripcion_bp.route("/contingencia", methods=["POST"])
def crear_contingencia():

    datos = request.get_json()

    resultado = service.registrar_contingencia(datos)

    return jsonify({
        "mensaje": "Acceso contingencial registrado",
        "contingencia": {
            "id": resultado.id,
            "dni": resultado.dni,
            "motivo": resultado.motivo
        }
    }), 201



@suscripcion_bp.route("/contingencia", methods=["GET"])
def listar_contingencia():

    contingencias = service.listar_contingencias()

    lista = []

    for contingencia in contingencias:
        lista.append({
            "id": contingencia.id,
            "dni": contingencia.dni,
            "motivo": contingencia.motivo
        })

    return jsonify(lista), 200