'''
Calcular el promedio de 5 calificaciones
'''

print("Bienvenido al sistema de calificaciones")


promedio = 0
for i in range(5):
    calificacion = float(input(f"Ingrese la calificacion N°: {i + 1}\n"))
    promedio = promedio + calificacion

promedio = promedio / 5

print("El promedio de la calificacion es:",promedio)