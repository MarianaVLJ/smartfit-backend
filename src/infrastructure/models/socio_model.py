from src.infrastructure.database import db

class SocioModel(db.Model):
    __tablename__ = 'socios'

    dni = db.Column(db.String(8), primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    plan = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "dni": self.dni,
            "nombres": self.nombres,
            "email": self.email,
            "plan": self.plan,
            "estado": self.estado
        }