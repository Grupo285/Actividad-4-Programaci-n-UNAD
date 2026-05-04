"""
Registro de eventos y errores en archivo.
"""

from datetime import datetime

def registrar_log(mensaje: str) -> None:
    """Guarda un mensaje con timestamp en logs.txt"""
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {mensaje}\n")