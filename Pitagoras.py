'''
Calcular e imprimir el valor de la hipotenusa de un triangulo rectangulo ingresando sus catetos
'''
import math

cateto_opuesto = float(input("Ingrese el cateto opuesto"))
cateto_adyacente = float(input("Ingresa el cateto adyacente"))

hipotenusa = cateto_adyacente * cateto_adyacente

hipotenusa = math.pow(hipotenusa,2)

print("La hipotenusa del triangulo es:",hipotenusa)