"""
Servicios derivados (herencia + polimorfismo).
"""

from servicio import Servicio
from excepciones import ServicioError

class Sala(Servicio):
    def calcular_costo(self, horas: int = 1, **kwargs) -> float:
        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a 0")
        return self.precio_base * horas

    def descripcion(self) -> str:
        return f"Reserva de sala: {self.nombre}"


class Equipo(Servicio):
    def calcular_costo(self, dias: int = 1, **kwargs) -> float:
        if dias <= 0:
            raise ServicioError("Los días deben ser mayores a 0")
        return self.precio_base * dias

    def descripcion(self) -> str:
        return f"Alquiler de equipo: {self.nombre}"


class Asesoria(Servicio):
    def calcular_costo(self, horas: int = 1, urgencia: bool = False, **kwargs) -> float:
        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a 0")

        costo = self.precio_base * horas

        # Ejemplo de “sobrecarga” por parámetros opcionales
        if urgencia:
            costo *= 1.3  # recargo por urgencia

        return costo

    def descripcion(self) -> str:
        return f"Asesoría especializada: {self.nombre}"
    