from src.infrastructure.database import db


class Suscripcion(db.Model):

    __tablename__ = 'suscripciones'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    dni = db.Column(
        db.String(8),
        db.ForeignKey('socios.dni'),
        nullable=False
    )

    plan = db.Column(
        db.String(50),
        nullable=False
    )

    fecha_inicio = db.Column(
        db.String(20),
        nullable=False
    )



class Contingencia(db.Model):

    __tablename__ = 'contingencias'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    dni = db.Column(
        db.String(8),
        db.ForeignKey('socios.dni'),
        nullable=False
    )

    motivo = db.Column(
        db.String(100),
        nullable=False
    )