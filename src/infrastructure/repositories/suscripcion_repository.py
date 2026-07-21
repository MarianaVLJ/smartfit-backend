from src.infrastructure.models.suscripcion_model import Suscripcion, Contingencia
from src.infrastructure.database import db


class SuscripcionRepository:

    def crear_suscripcion(self, datos):

        nueva_suscripcion = Suscripcion(
            dni=datos["dni"],
            plan=datos["plan"],
            fecha_inicio=datos["fecha_inicio"]
        )

        db.session.add(nueva_suscripcion)
        db.session.commit()

        return nueva_suscripcion


    def obtener_suscripciones(self):

        return Suscripcion.query.all()



    def actualizar_suscripcion(self, id, datos):

        suscripcion = Suscripcion.query.get(id)

        if not suscripcion:
            return None

        suscripcion.plan = datos["plan"]

        db.session.commit()

        return suscripcion



    def eliminar_suscripcion(self, id):

        suscripcion = Suscripcion.query.get(id)

        if not suscripcion:
            return None

        db.session.delete(suscripcion)
        db.session.commit()

        return suscripcion



    def crear_contingencia(self, datos):

        nueva_contingencia = Contingencia(
            dni=datos["dni"],
            motivo=datos["motivo"]
        )

        db.session.add(nueva_contingencia)
        db.session.commit()

        return nueva_contingencia



    def obtener_contingencias(self):

        return Contingencia.query.all()