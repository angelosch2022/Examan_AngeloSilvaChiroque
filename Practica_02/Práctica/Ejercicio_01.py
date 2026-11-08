"""
1. Registro de personas (4 ptos)
    Requisitos:
    • Crear una clase Persona con los atributos nombre, edad, saldo y nacionalidad. La nacionalidad tendrá como valor inicial “Peruana”.
    • Implementar un método que permita registrar el nombre y la edad de una persona mediante la consola. Si la edad ingresada no es un número entero válido o es negativa, informar el problema y solicitar nuevamente el dato.
    • Implementar un método cumpleaños que incremente la edad en un año cada vez que se invoque.
    • Crear como mínimo dos objetos de la clase Persona, utilizar el método cumpleaños y mostrar las edades actualizadas.
    • Registrar el momento de creación de cada persona y mostrar, mediante una función, la fecha y hora de registro con precisión de minutos.
"""
from datetime import datetime
class Persona:
    def __init__(self,saldo, nombre="", edad=0):
        self.nombre=nombre
        self.edad=edad
        self.saldo=saldo
        self.nacionalidad="Peruana"
        self.fecha_registro=datetime.now()

    #metodos
    def registrar(self):
        self.nombre=input("Ingrese el nombre: ")
        while True:
            try:
                self.edad=int(input("Ingrese la edad: "))
                if self.edad<0:
                    print("La edad no puede ser negativa.")
                else:
                    break
            except ValueError:
                print("La edad debe ser un número entero.")

    def cumpleanios(self):
        self.edad+=1

#objetos
if __name__=="__main__":
    persona_1=Persona(600)
    persona_1.registrar()
    persona_2=Persona(300)
    persona_2.registrar()
    #
    print(f"Edad inicial de {persona_1.nombre} es: {persona_1.edad}")
    print(f"Edad inicial de {persona_2.nombre} es: {persona_2.edad}")
    print("***********************************")
    persona_1.cumpleanios()
    persona_2.cumpleanios()
    #
    print(f"Edad actualizada de {persona_1.nombre} es: {persona_1.edad}")
    print(f"Edad actualizada de {persona_2.nombre} es: {persona_2.edad}")
    #
    print(f"Fecha de registro de {persona_1.nombre} es: {persona_1.fecha_registro.strftime('%Y-%m-%d %H:%M')}")
    print(f"Fecha de registro de {persona_2.nombre} es: {persona_2.fecha_registro.strftime('%Y-%m-%d %H:%M')}")