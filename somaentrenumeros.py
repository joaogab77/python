def somar_pares():
    soma = 0
    for num in range (50,100):
        if num % 2 == 0:
            soma += num
    return soma

resultado = somar_pares()
print ("A soma dos numeros pares entre 50 e 100 é:", resultado)


