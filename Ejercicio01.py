import math
print("INGRESAR LOS NUMEROS CON SU SIGNO")
a=int(input('Ingrese la primera constante de x²: '))
b=int(input('Ingrese la segunda constante de x: '))
c=int(input('Ingrese el termino independiente: '))
x1= (-b + math.sqrt(b*b-4*a*c))/(2*a)
x2= (-b - math.sqrt(b*b-4*a*c))/(2*a)

print("La ecuacion de segundo grado es: ",a,"x²",b,"x",c)
print("El primer resultado es la raiz: ",x1)
print("El segundo resultado es la raiz: ",x2)