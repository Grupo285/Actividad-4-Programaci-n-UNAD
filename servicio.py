"""
Clase abstracta Servicio.
Define el contrato de los servicios.
"""

from abc import ABC, abstractmethod
from excepciones import ServicioError

class Servicio(ABC):
    def __init__(self, nombre: str, precio_base: float):
        if not nombre or not nombre.strip():
            raise ServicioError("El servicio debe tener un nombre válido")
        if precio_base <= 0:
            raise ServicioError("El precio base debe ser mayor a 0")

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, **kwargs) -> float:
        """Calcula el costo del servicio."""
        pass

    @abstractmethod
    def descripcion(self) -> str:
        """Descripción del servicio."""
        pass