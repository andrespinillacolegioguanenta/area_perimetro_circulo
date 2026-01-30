# Programa para calcular el area y el perimetro del circulo

# Librerian
import math

print ("------------------------------------------------")
print ("---------area y perimetro del circulo-----------")
print ("------------------------------------------------")

# input
r = input ("Digite el valor del radio: ") 
r = int (r)

# Procesing
a = math.pi*r*r
p = 2*math.pi*r

# OUTPUT
print("-------------------------------")
print("----------Resultado------------")
print("-------------------------------")
print("El area del circulo es:"+str(a))
print("El valor de el perimetroes:"+str(p))
print("----------------------------------")