dicc= {"A": "","B": "","C": "","D":"","F":"","G":"","H":"","I":"","J":"","K":""}

for i in dicc:
    edad = int(input("Introduce la edad de "+i+" : "))
    dicc[i]= edad 

for l in dicc:
    if int(dicc[l]) > 20:
        print(l+" tiene más de 20 años")

print(dicc)