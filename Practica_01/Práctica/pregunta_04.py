"""
4. Registro de participantes con listas (3 ptos)
    Crea una lista vacía y realiza lo siguiente:
        - Agrega los nombres de tres participantes.
        - Inserta un nuevo participante en la segunda posición.
        - Actualiza el nombre del primer participante.
        - Elimina uno de los participantes.
        - Muestra la lista final y la cantidad de participantes registrados.
        - No utilizar ciclos ni recorridos.
"""
lista_participantes = []

lista_participantes.append("Angelo")
lista_participantes.append("Maria")
lista_participantes.append("José")

lista_participantes.insert(1, "Rodrigo")

lista_participantes[0] = "Carlos"

lista_participantes.remove("José")
print("Lista final:", lista_participantes)
print("Cantidad de participantes:", len(lista_participantes))
