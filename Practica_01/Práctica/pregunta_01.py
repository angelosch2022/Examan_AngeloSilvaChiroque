"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (3 ptos)
    Reglas:
    - Asignar en variables los datos de tu nombre, salario, edad y compañía para un
    usuario e identificar sus tipos de variables
    - Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
    conversión de datos
    - Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
    tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
    tiene un bono del 5% en el mes diciembre”
    - Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
    salario, según corresponda
"""
nombre="Angelo"
salario=5000
edad="37"
compañia="ABC"

t_nombre=type(nombre)
t_salario=type(salario)
t_edad=type(edad)
t_compañia=type(compañia)
edad_int = int(edad)
if(edad_int>30):
    print("Usted tiene un bono de 10% en el mes de diciembre")
    bono=salario*0.10

else:
    print("Usted tiene un bono del 5% en el mes de diciembre")
    bono=salario*0.05
    
bono_final = salario**2 + bono
print("El bono final es: {}".format(bono_final))
