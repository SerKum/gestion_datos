listN = ['Sergio','Carlos','Marta','Sandra','Ramón']

letra = str(input("Introduce la inicial : "))

for i in listN: 
    if i[0] == letra:
        print(i+" comienza por la letra "+letra)