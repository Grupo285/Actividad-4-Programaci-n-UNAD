"""
Excepciones personalizadas del sistema.
"""

class ErrorSistema(Exception):
    """Base para todos los errores del sistema."""
    pass

class ClienteError(ErrorSistema):
    """Errores relacionados con Cliente."""
    pass

class ServicioError(ErrorSistema):
    """Errores relacionados con Servicio."""
    pass

class ReservaError(ErrorSistema):
    """Errores relacionados con Reserva."""
    pass