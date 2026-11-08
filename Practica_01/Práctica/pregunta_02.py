"""
- Caso: Reporte de calificaciones:
Se tiene un alumno con calificaciones en tres cursos:
Matemáticas: 17, Ciencia: 14, Historia: 15
Cada curso tiene un peso diferente en la nota final:
Matemáticas: 40%, Ciencia: 30%, Historia: 30%
Realizar lo que se pide a continuación:
Calcula la nota final ponderada del alumno.
Muestra un mensaje como: "La nota final es: 15.6" con 1 decimal.
Evalúa si el alumno aprueba (nota final >= 13.0). Muestra un mensaje booleano:
"¿Aprobado?: True" o "¿Aprobado?: Sí"
Genera una cadena resumen que diga:
"El estudiante obtuvo una nota final de 15.6 y su estado final es: Aprobado"
En caso no apruebe indicar lo contrario en los mensajes.
"""
nota_matematicas=17
nota_ciencia=14
nota_historia=15

peso_matematicas=0.4
peso_ciencia=0.3
peso_historia=0.3

nota_ponderada_final=(nota_matematicas*peso_matematicas)+(nota_ciencia*peso_ciencia)+(nota_historia*peso_historia)
print("La nota final es: {:.1f}".format(nota_ponderada_final))
if nota_ponderada_final>=13.0:
    aprobado: True
    estado_final="Aprobado"
else:
    aprobado: False
    estado_final="Reprobado"

print("El estudiante obtuvo una nota final de {:.1f} y su estado final es: {}".format(nota_ponderada_final, estado_final))