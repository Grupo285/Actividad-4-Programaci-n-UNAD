"""
Clase Reserva.
Integra cliente y servicio.
"""

from excepciones import ReservaError
from logger import registrar_log
from cliente import Cliente
from servicio import Servicio

class Reserva:
    def __init__(self, cliente: Cliente, servicio: Servicio):
        if not isinstance(cliente, Cliente):
            raise ReservaError("Cliente inválido")

        if not isinstance(servicio, Servicio):
            raise ReservaError("Servicio inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "pendiente"

    def confirmar(self):
        try:
            if self.estado != "pendiente":
                raise ReservaError("La reserva ya fue procesada")

            self.estado = "confirmada"

            registrar_log(
                f"Reserva confirmada para {self.cliente.get_nombre()}"
            )

        except Exception as e:
            registrar_log(f"Error confirmando reserva: {str(e)}")
            raise

    def cancelar(self):
        try:
            if self.estado == "cancelada":
                raise ReservaError("La reserva ya está cancelada")

            self.estado = "cancelada"

            registrar_log(
                f"Reserva cancelada para {self.cliente.get_nombre()}"
            )

        except Exception as e:
            registrar_log(f"Error cancelando reserva: {str(e)}")
            raise

    def procesar_pago(self, **kwargs):
        try:
            if self.estado == "cancelada":
                raise ReservaError(
                    "No se puede pagar una reserva cancelada"
                )

            costo = self.servicio.calcular_costo(**kwargs)

        except Exception as e:
            registrar_log(f"Error procesando pago: {str(e)}")
            raise ReservaError("Error en el pago") from e

        else:
            registrar_log(f"Pago realizado correctamente: {costo}")
            return costo

        finally:
            registrar_log("Proceso de pago finalizado")