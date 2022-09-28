actual = int(input("Introduce el año actual : "))
i = 1
listN = []
listA = []
while i <= 3 :
    listN.append(str(input("Introduce el nombre : ")))
    listA.append(int(input("Introduce el año de nacimiento : ")))
    i+=1

for l in range(len(listN)):
    anyos = actual-listA[l]
    print(listN[l]+" cumple "+str(anyos)+" años")