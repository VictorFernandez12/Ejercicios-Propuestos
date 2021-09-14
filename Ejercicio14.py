import math
x1=int(input("Ingrese el primer valor de la primera coordenada X1:"))
y1=int(input("Ingrese el segundo valor de la primera coordenada y1:"))
x2=int(input("Ingrese el primer valor de la segunda coordenada X2:"))
y2=int(input("Ingrese el segundo valor de la segunda coordenada y2:"))
z1=int(input("Ingrese el primer valor de la tercera coordenada z1:"))
z2=int(input("Ingrese el segundo valor de la tercera coordenada z2:"))
d=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)+math.pow((z2-z1),2))
print("La distancia entre 2 puntos es:",d)