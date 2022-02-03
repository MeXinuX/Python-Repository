'''
Calcular el promedio de 5 calificaciones
'''

print("Bienvenido al sistema de calificaciones")


promedio = 0
i = 1
for i in range(5):
    print("Ingrese la calificacion N°:",i + 1)
    calificacion = float(input())
    promedio = promedio + calificacion

promedio = promedio / 5

print("El promedio de la calificacion es:",promedio)