horas=int(input('Ingrese el número de horas: '))
s=horas/(24*7)
d=horas%(24*7)/24
h=horas%24
print("La cantidad de ",horas,"horas equivale a: ",int(s),"semana(s)",int(d),"día(s)","y",int(h),"hora(s)")