cadena = str(input("Ingresa una frase : "))
mayusculas = 0
for letra in cadena:
    if letra.isupper() == True:
        mayusculas+=1
print("Hay un total de "+str(mayusculas)+" mayúsculas")
