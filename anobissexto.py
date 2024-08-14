ano = int(input('Digite o ano para saber se é bissexto ou não: '))
if ano % 4 == 0:
    if ano % 400 == 0:
        print("ano Bissexto")
    else:
            if ano % 100 == 0:
                print("ano não Bissexto")
            else:
                print("ano Bissexto")
else:
     print('ano Bissexto')
print('FIM')