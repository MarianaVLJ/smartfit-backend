from flask import Blueprint, request, jsonify
from src.application.services.suscripcion_service import SuscripcionService


suscripcion_bp = Blueprint("suscripcion_bp", __name__)

service = SuscripcionService()


# ==========================
# CREAR SUSCRIPCIÓN
# ==========================

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



# ==========================
# LISTAR SUSCRIPCIONES
# ==========================

@suscripcion_bp.route("/suscripciones", methods=["GET"])
def listar_suscripciones():

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



# ==========================
# ACTUALIZAR PLAN
# ==========================

@suscripcion_bp.route("/suscripciones/<int:id>", methods=["PUT"])
def actualizar_suscripcion(id):

    datos = request.get_json()

    resultado = service.actualizar_suscripcion(id, datos)

    if resultado is None:
        return jsonify({
            "mensaje": "Suscripción no encontrada"
        }), 404


    return jsonify({
        "mensaje": "Plan actualizado correctamente",
        "suscripcion": {
            "id": resultado.id,
            "dni": resultado.dni,
            "plan": resultado.plan,
            "fecha_inicio": resultado.fecha_inicio
        }
    }), 200



# ==========================
# ELIMINAR SUSCRIPCIÓN
# ==========================

@suscripcion_bp.route("/suscripciones/<int:id>", methods=["DELETE"])
def eliminar_suscripcion(id):

    resultado = service.eliminar_suscripcion(id)

    if resultado is None:
        return jsonify({
            "mensaje": "Suscripción no encontrada"
        }), 404


    return jsonify({
        "mensaje": "Suscripción eliminada correctamente"
    }), 200



# ==========================
# CREAR CONTINGENCIA
# ==========================

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



# ==========================
# LISTAR CONTINGENCIAS
# ==========================

@suscripcion_bp.route("/contingencia", methods=["GET"])
def listar_contingencias():

    contingencias = service.listar_contingencias()

    lista = []

    for contingencia in contingencias:
        lista.append({
            "id": contingencia.id,
            "dni": contingencia.dni,
            "motivo": contingencia.motivo
        })

    return jsonify(lista), 200