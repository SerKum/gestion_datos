palabra=str(input("Introduce una palabra : "))

def contar_vocales(p):
    contadorA=0
    contadorE=0
    contadorI=0
    contadorO=0
    contadorU=0
    for i in palabra:
        if (i.lower() == 'a'):
            contadorA+=1
        elif i.lower() == 'e':
            contadorE+=1
        elif i.lower() == 'i':
            contadorI+=1
        elif i.lower() == 'o':
            contadorO+=1
        elif i.lower() == 'u':
            contadorU+=1
    print("La palabra "+palabra+" tiene : "+str(contadorA)+" A, "+str(contadorE)+" E, "+str(contadorI)+" I, "+str(contadorO)+" O, "+str(contadorU)+" U")

contar_vocales(palabra)