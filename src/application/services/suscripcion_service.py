from src.infrastructure.repositories.suscripcion_repository import SuscripcionRepository


class SuscripcionService:

    def __init__(self):
        self.repository = SuscripcionRepository()


    def crear_suscripcion(self, datos):
        return self.repository.crear_suscripcion(datos)


    def listar_suscripciones(self):
        return self.repository.obtener_suscripciones()


    def registrar_contingencia(self, datos):
        return self.repository.crear_contingencia(datos)


    def listar_contingencias(self):
        return self.repository.obtener_contingencias()