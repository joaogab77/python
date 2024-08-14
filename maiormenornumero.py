n1 = int(input('Digite um número'))
n2 = int(input('Digite outro'))
n3 = int(input('Digite mais um'))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')