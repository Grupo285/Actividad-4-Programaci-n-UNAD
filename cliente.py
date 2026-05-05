"""
Clase Cliente con encapsulación y validaciones robustas.
"""

from excepciones import ClienteError

class Cliente:
    def __init__(self, nombre: str, email: str):
        # Validaciones
        if not nombre or len(nombre.strip()) < 3:
            raise ClienteError("El nombre debe tener al menos 3 caracteres")

        if "@" not in email or "." not in email:
            raise ClienteError("Correo electrónico inválido")

        self.__nombre = nombre.strip()
        self.__email = email.strip()

    # Encapsulación (getters)
    def get_nombre(self) -> str:
        return self.__nombre

    def get_email(self) -> str:
        return self.__email

    # Representación
    def __str__(self) -> str:
        return f"Cliente({self.__nombre}, {self.__email})"