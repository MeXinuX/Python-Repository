'''
La Fonda de la esquinja desea automatizar el proceso para agregar el 16% de IVA(impuesto al valor agregado) a las compras que se realizan durante el dia
'''

from functools import total_ordering


subtotal = float(input("Ingrese el total de la compra\n"))

iva = round(subtotal * 0.16,2)
total = round(subtotal + iva,2)

print("El subtotal es:",subtotal,"\nIVA:",iva,"\nTotal:",total)