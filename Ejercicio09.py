RC=int(input("Ingrese la cantidad de respuestas correctas: "))
RI=int(input("Ingrese la cantidad de respuestas incorrectas: "))
RB=int(input("Ingrese la cantidad de respuestas en blanco: "))
PRC=RC*3
PRI=RI*(-1)
PRB=RB*0
print("La cantidad de presguntas son:",RC+RI+RB)
print("El puntaje final del alumno es:",(PRC+PRI+PRB))