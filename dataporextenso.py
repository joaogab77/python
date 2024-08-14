# Funções auxiliares para converter números para texto
def numero_por_extenso(num):
    unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    especiais = {
        10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis",
        17: "dezessete", 18: "dezoito", 19: "dezenove"
    }

    if num < 10:
        return unidades[num]
    elif 10 <= num < 20:
        return especiais[num]
    else:
        dezena, unidade = divmod(num, 10)
        if unidade == 0:
            return dezenas[dezena]
        else:
            return f"{dezenas[dezena]} e {unidades[unidade]}"


def ano_por_extenso(ano):
    if ano < 2000:
        return numero_por_extenso(ano)
    else:
        ano = str(ano)
        return f"{numero_por_extenso(int(ano[:2]))} mil e {numero_por_extenso(int(ano[2:]))}"


def data_por_extenso(data):
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    dia, mês, ano = data.split('/')
    dia = int(dia)
    mês = int(mês)
    ano = int(ano)

    dia_extenso = numero_por_extenso(dia)
    mês_extenso = meses[mês - 1]
    ano_extenso = ano_por_extenso(ano)

    return f"{dia_extenso} de {mês_extenso} de {ano_extenso}"


def valida_data(data):
    try:
        dia, mês, ano = data.split('/')
        dia = int(dia)
        mês = int(mês)
        ano = int(ano)

        if dia < 1 or dia > 31:
            return False
        if mês < 1 or mês > 12:
            return False
        if ano < 1:
            return False
        return True
    except ValueError:
        return False


def converte_data():
    while True:
        data = input("Digite uma data (DD/MM/AAAA): ")
        if valida_data(data):
            data_extenso = data_por_extenso(data)
            print(f"Data por extenso: {data_extenso}")
            return data_extenso
        else:
            print("Formato de data inválido. Tente novamente.")


def listar_datas(datas):
    if not datas:
        print("Nenhuma data foi convertida ainda.")
    else:
        print("Datas convertidas por extenso:")
        for data in datas:
            print(data)


def salvar_datas(datas):
    nome_arquivo = input("Digite o nome do arquivo para salvar as datas: ")
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for data in datas:
                arquivo.write(data + "\n")
        print(f"Datas salvas no arquivo '{nome_arquivo}'.")
    except IOError:
        print("Erro ao salvar o arquivo. Verifique se o arquivo está aberto em outro programa.")


def menu():
    datas_convertidas = []

    while True:
        print("\nMenu de Opções:")
        print("1 - Converter Data")
        print("2 - Listar Datas por extenso")
        print("3 - Salvar Datas em Arquivo")
        print("4 - Sair")

        opção = input("Escolha uma opção: ")

        if opção == '1':
            data_extenso = converte_data()
            datas_convertidas.append(data_extenso)
        elif opção == '2':
            listar_datas(datas_convertidas)
        elif opção == '3':
            salvar_datas(datas_convertidas)
        elif opção == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executa o programa
menu()
