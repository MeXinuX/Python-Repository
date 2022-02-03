'''
Calcular N pies a centimetros.tomando en cuenta que un pie tiene 12 pulgadas y una pulgada equivale a 2.54 centimetros
'''

pies = float(input("Ingrese la cantidad de pies"))

pulgadas = pies * 12

centimetros = pulgadas + 2.54

print("El resultado de la conversion es",centimetros,"Centimetros")