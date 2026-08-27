import math as m

a = float(input("Indroduzca el a"))
b = float(input("Indroduzca el b"))
n = float(input("Indroduzca el numero de pasos"))
dx = (b-a)/n 
suma = 0

for i in range(n):
    x = a + i*dx
    y = m.sin(x)**2 + x
    suma = suma + y*dx
print(f"su aproximacion del area bajo la curva por suma de riemman es {suma}") 