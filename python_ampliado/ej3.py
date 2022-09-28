def filtrar_palabras(lista,entero):
    list = []
    for pal in lista:
        if len(pal) > entero:
            list.append(pal)
    print(list)

palabras = str(input("Introduce palabras : "))
palabras = palabras.split(',')
numero = int(input("Introduce un numero :"))

filtrar_palabras(palabras,numero)