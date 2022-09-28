anyo= int(input("Introduce un año: "))

def es_bisiesto(a):
    if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
	    print("Es bisiesto")
    else:
	    print("No es bisiesto")
es_bisiesto(anyo)