x=True
y=False
z=True
print("El valor de: (X && Y) || (X && Z) es:",(x and y)or(x and z))
print("EL valo de: (X || !Y) && (!X || Z) es:",(x or not y)and(not x or z))
print("El valor de: X || Y && Z es",(x or y and z))
print("El valor de: !(X || Y) && Z es:",(not(x or y)and z))
print("El valor de X || Y || X && !Z && !Y es:",(x or y or x and not z and not y))
print("El valor de !X || !Y || Z && X && !Y es:",(not x or not y or z and x and not y))