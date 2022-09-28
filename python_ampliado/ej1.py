numeros = str(input("Introduce una lista de numeros : "+"\n"))

numeros = numeros.split(',')


def max_in_list(numeros):
    max = 0
    for num in numeros:
        num = int(num)
        if num > max :
            max=num
    print(max)

max_in_list(numeros)