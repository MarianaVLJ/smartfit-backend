from src.infrastructure.repositories.socio_repository import SocioRepository

class SocioService:
    def __init__(self):
        self.repository = SocioRepository()

    def registrar_socio(self, datos):
        datos['estado'] = 'Activo'
        return self.repository.guardar(datos)

    def obtener_socio(self, dni):
        return self.repository.buscar_por_dni(dni)

    def modificar_socio(self, dni, datos):
        return self.repository.actualizar(dni, datos)

    def dar_de_baja_socio(self, dni):
        return self.repository.eliminar(dni)