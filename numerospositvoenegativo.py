def separar_numeros(lista):
    positivos = []
    negativos = []

    for numero in lista:
        if numero > 0:
            positivos.append(numero)
        else:
            negativos.append(numero)

    return positivos, negativos

numeros = [11, -6, 7, -1, 0, -2, 8]
positivos, negativos = separar_numeros(numeros)

print ("Números positivos",positivos)
print ("Números negativos",negativos)