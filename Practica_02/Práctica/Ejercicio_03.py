"""
3. Funciones y manejo de excepciones (3 ptos)
Requisitos:
    • Crear una función que solicite al usuario dos valores numéricos por consola y los retorne para utilizarlos en las operaciones.
    • Crear una función que reciba dos valores como parámetros, realice una división y retorne el resultado.
    • Crear una función que reciba dos valores como parámetros, realice una suma y retorne el resultado.
    • Solicitar al usuario cuántos elementos desea registrar (N) y crear una función que reciba esos datos ingresados por consola, los almacene en una lista y retorne la lista. 
    • Solicitar al usuario el índice que desea consultar y crear una función que reciba la lista y dicho índice como parámetros para retornar el elemento correspondiente. 
    • Controlar los errores provocados por entradas no numéricas, divisiones entre cero, operaciones entre tipos incompatibles y consultas a posiciones inexistentes de la lista. 
    • Cuando se produzca un error, mostrar un mensaje descriptivo y permitir un nuevo intento de la operación correspondiente.
    • Utilizar else y finally en al menos una de las operaciones realizadas.
    • Ejecutar las funciones creadas utilizando los datos proporcionados por el usuario y mostrar por consola los resultados de las operaciones correctas. Incluir 3 pruebas con datos válidos e inválidos.
"""
def solicitar_valores():
    while True:
        try:
            valor1=float(input("Ingrese el primer valor: "))
            valor2=float(input("Ingrese el segundo valor: "))
            return valor1, valor2
        except ValueError:
            print("Los valores deben ser numéricos. Intente nuevamente.")
def dividir(numero_01, numero_02):
    try:
        resultado = round(numero_01/numero_02,4)
    except ZeroDivisionError:
        print("Error: División entre cero no permitida.")
        return None
    except TypeError:
        print("Error: Tipos incompatibles para la división")
        return None
    else:
        return resultado
    finally:
        print("división finalizada")

def sumar(numero_01, numero_02):
    return numero_01 + numero_02
   

def solicitar_cantidad():
    cantidad = input("Ingrese la cantidad de elementos a registrar: ")
    while True:
        try:
            cantidad=int(cantidad)
            if cantidad<=0:
                print("La cantidad debe ser mayor a cero")
                cantidad = input("Ingrese la cantidad de elementos: ")
            else:
                break
        except ValueError:
            print("La cantidad debe ser un número entero")
            cantidad = input("Ingrese la cantidad de elementos a registrar: ")
    return cantidad

def registrar_elementos(n):
    elementos = []
    for i in range(n):
        while True:
            try:
                valor = float(input(f"Ingrese el elemento {i+1}: "))
                elementos.append(valor)
                break
            except ValueError:
                print("El valor debe ser numérico. Intente nuevamente")
    return elementos

#ejecución
#datos válidos
valor1, valor2 = solicitar_valores()
print(f"Valores ingresados: {valor1}, {valor2}")
div = dividir(valor1, valor2)
print(f"Resultado de la división: {div}")
suma = sumar(valor1, valor2)
print(f"Resultado de la suma: {suma}")

cantidad = solicitar_cantidad()
elementos = registrar_elementos(cantidad)
print(f"Elementos registrados: {elementos}")
