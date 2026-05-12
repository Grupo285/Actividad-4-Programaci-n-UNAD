"""
Archivo principal del sistema.
Simula operaciones válidas e inválidas.
"""

from cliente import Cliente
from servicios import Sala, Equipo, Asesoria
from reserva import Reserva

def ejecutar_pruebas():

    print("=== INICIO DEL SISTEMA ===")

    # CASO 1
    c1 = Cliente("Ana", "ana@gmail.com")
    print(c1)

    # CASO 2
    try:
        Cliente("A", "correo")
    except Exception as e:
        print("Error esperado:", e)

    # CASO 3
    sala = Sala("Sala VIP", 100)

    # CASO 4
    try:
        Sala("Sala Mala", -10)
    except Exception as e:
        print("Error esperado:", e)

    # CASO 5
    reserva1 = Reserva(c1, sala)
    reserva1.confirmar()

    # CASO 6
    pago1 = reserva1.procesar_pago(horas=3)
    print("Pago sala:", pago1)

    # CASO 7
    reserva1.cancelar()

    # CASO 8
    try:
        reserva1.procesar_pago(horas=2)
    except Exception as e:
        print("Error esperado:", e)

    # CASO 9
    asesoria = Asesoria("Consultoría", 150)

    reserva2 = Reserva(c1, asesoria)

    reserva2.confirmar()

    pago2 = reserva2.procesar_pago(
        horas=2,
        urgencia=True
    )

    print("Pago asesoría:", pago2)

    # CASO 10
    equipo = Equipo("Laptop", 80)

    reserva3 = Reserva(c1, equipo)

    reserva3.confirmar()

    pago3 = reserva3.procesar_pago(dias=2)

    print("Pago equipo:", pago3)

    print("=== FIN DEL SISTEMA ===")


if __name__ == "__main__":
    ejecutar_pruebas()