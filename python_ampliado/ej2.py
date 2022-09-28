palabras = str(input("Introduce una lista de palabras: "+"\n"))

palabras=palabras.split(',')

def mas_larga():
    larga = ''
    for pal in palabras:
        if len(pal) > len(larga):
            larga = pal
    print(larga)

mas_larga()