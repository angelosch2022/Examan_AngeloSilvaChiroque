"""
2. Transferencias entre personas (3 ptos)
    Requisitos:
    • Utilizar la clase Persona del ejercicio anterior y su atributo saldo para simular transferencias entre dos personas.
    • Implementar los métodos necesarios para consultar el saldo y efectuar una transferencia de dinero de una persona a otra.
    • Cada transferencia válida deberá descontar el monto de la persona que envía el dinero y sumarlo al saldo de quien lo recibe.
    • No permitir transferencias con montos no numéricos, menores o iguales a cero, ni superiores al saldo disponible. Informar al usuario cuando la operación no pueda realizarse y conservar los saldos sin cambios.
    • Demostrar el funcionamiento con dos personas, incluyendo al menos una transferencia válida y un intento de transferencia rechazado.
"""
from Ejercicio_01 import Persona
def consultar_saldo(persona):
    print(f"El saldo de {persona.nombre} es: {persona.saldo}")

def transferir(emisor, receptor, monto):
    try:
        monto = float(monto)
        if monto<=0:
            print("El monto a enviardebe ser mayor a cero")
        elif monto>emisor.saldo:
            print(f"Rechazado, saldo insuficiente")
        else:
            emisor.saldo -= monto
            receptor.saldo += monto
            print(f"Transferencia de {monto} realizada con éxito.")
    except ValueError:
        print("El monto debe ser un número.")

persona_1=Persona(400)
persona_1.registrar()
persona_2=Persona(300)
persona_2.registrar()
print("***********************************")
print("*****transferencias*****")
consultar_saldo(persona_1)
consultar_saldo(persona_2)

transferir(persona_1, persona_2, 100)

consultar_saldo(persona_1)
consultar_saldo(persona_2)
print("***********************************")
transferir(persona_1, persona_2, 500)

consultar_saldo(persona_1)
consultar_saldo(persona_2)