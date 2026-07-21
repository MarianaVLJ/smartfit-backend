class SuscripcionService:

    def __init__(self):
        self.suscripciones = []
        self.contingencias = []

    def crear_suscripcion(self, datos):
        self.suscripciones.append(datos)
        return datos

    def listar_suscripciones(self):
        return self.suscripciones

    def registrar_contingencia(self, datos):
        self.contingencias.append(datos)
        return datos

    def listar_contingencias(self):
        return self.contingencias