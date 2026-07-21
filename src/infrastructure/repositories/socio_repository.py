from src.infrastructure.database import db
from src.infrastructure.models.socio_model import SocioModel

class SocioRepository:
    def guardar(self, socio_data):
        socio = SocioModel(
            dni=socio_data['dni'],
            nombres=socio_data['nombres'],
            email=socio_data['email'],
            plan=socio_data['plan'],
            estado=socio_data['estado']
        )
        db.session.add(socio)
        db.session.commit()
        return socio.to_dict()

    def buscar_por_dni(self, dni):
        socio = SocioModel.query.get(dni)
        return socio.to_dict() if socio else None

    def actualizar(self, dni, datos):
        socio = SocioModel.query.get(dni)
        if socio:
            if 'plan' in datos:
                socio.plan = datos['plan']
            if 'estado' in datos:
                socio.estado = datos['estado']
            db.session.commit()
            return socio.to_dict()
        return None

    def eliminar(self, dni):
        socio = SocioModel.query.get(dni)
        if socio:
            db.session.delete(socio)
            db.session.commit()
            return True
        return False