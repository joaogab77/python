#Inicializa uma lista vazia para armazenar os contatos da agenda
agenda = []
alterada = False  # Flag para indicar se a agenda foi alterada

#Função para pedir o nome do contato, com um valor padrão opcional
def pede_nome(padrão=""):
    nome = input("Nome: ")  #Solicita o nome ao usuário
    if nome == "":  #Se o nome for vazio, utiliza o valor padrão
        nome = padrão
    return nome  #Retorna o nome obtido

#Função para pedir o telefone do contato, com um valor padrão opcional
def pede_telefone(padrão=""):
    telefone = input("Telefone: ")  #Solicita o telefone ao usuário
    if telefone == "":  #Se o telefone for vazio, utiliza o valor padrão
        telefone = padrão
    return telefone  #Retorna o telefone obtido

#Função para pedir o endereço do contato, com um valor padrão opcional
def pede_endereço(padrão=""):
    endereço = input("Endereço: ")  #Solicita o endereço ao usuário
    if endereço == "":  #Se o endereço for vazio, utiliza o valor padrão
        endereço = padrão
    return endereço  #Retorna o endereço obtido

#Função para pedir a cidade do contato, com um valor padrão opcional
def pede_cidade(padrão=""):
    cidade = input("Cidade: ")  #Solicita a cidade ao usuário
    if cidade == "":  #Se a cidade for vazia, utiliza o valor padrão
        cidade = padrão
    return cidade  #Retorna a cidade obtida

#Função para pedir a unidade federativa (UF) do contato, com um valor padrão opcional
def pede_uf(padrão=""):
    uf = input("UF: ")  #Solicita a UF ao usuário
    if uf == "":  #Se a UF for vazia, utiliza o valor padrão
        uf = padrão
    return uf  #Retorna a UF obtida

#Função para exibir os dados de um contato
def mostra_dados(nome, telefone, endereço, cidade, uf):
    print(f"Nome: {nome} Telefone: {telefone} Endereço: {endereço} Cidade: {cidade} UF: {uf}")

#Função para solicitar o nome de um arquivo ao usuário
def pede_nome_arquivo():
    return input("Nome do arquivo: ")

#Função para pesquisar um nome na agenda
def pesquisa(nome):
    mnome = nome.lower()  #Converte o nome para minúsculas para comparação
    for p, e in enumerate(agenda):  #Percorre a lista da agenda
        if e[0].lower() == mnome:  #Compara o nome informado com os nomes na agenda
            return p  #Retorna a posição do nome na lista se encontrado
    return None  #Retorna None se o nome não for encontrado

#Função para verificar se o nome já existe na agenda
def verifica_repetição(nome):
    if pesquisa(nome) is not None:  #Verifica se o nome já está na agenda
        print("Erro: Nome já existe na agenda.")
        return True  #Retorna True se o nome já existir
    return False  #Retorna False se o nome não existir

#Função para adicionar um novo contato à agenda
def novo():
    global agenda, alterada
    nome = pede_nome()  #Pede o nome do novo contato
    if verifica_repetição(nome):  #Verifica se o nome já existe na agenda
        return  #Sai da função se o nome já existir
    telefone = pede_telefone()  #Pede o telefone do novo contato
    endereço = pede_endereço()  #Pede o endereço do novo contato
    cidade = pede_cidade()  #Pede a cidade do novo contato
    uf = pede_uf()  #Pede a UF do novo contato
    agenda.append([nome, telefone, endereço, cidade, uf])  #Adiciona o novo contato à agenda
    alterada = True  #Marca a agenda como alterada

#Função para confirmar uma operação (S/N)
def confirma(operação):
    while True:
        opção = input(f"Confirma {operação} (S/N)? ").upper()  #Solicita confirmação do usuário
        if opção in "SN":  #Verifica se a opção é válida
            return opção  #Retorna a opção escolhida
        else:
            print("Resposta inválida. Escolha S ou N.")

#Função para apagar um contato da agenda
def apaga():
    global agenda, alterada
    nome = pede_nome()  #Pede o nome do contato a ser apagado
    p = pesquisa(nome)  #Pesquisa o nome na agenda
    if p is not None:  #Se o nome for encontrado
        if confirma("apagamento") == "S":  #Solicita confirmação para apagar
            del agenda[p]  #Apaga o contato da agenda
            alterada = True  #Marca a agenda como alterada
    else:
        print("Nome não encontrado.")  #Informa que o nome não foi encontrado

#Função para alterar os dados de um contato
def altera():
    global alterada
    p = pesquisa(pede_nome())  #Pesquisa o nome do contato a ser alterado
    if p is not None:  #Se o nome for encontrado
        nome = agenda[p][0]  #Obtém o nome atual do contato
        telefone = agenda[p][1]  #Obtém o telefone atual do contato
        endereço = agenda[p][2]  #Obtém o endereço atual do contato
        cidade = agenda[p][3]  #Obtém a cidade atual do contato
        uf = agenda[p][4]  #Obtém a UF atual do contato
        print("Encontrado:")  #Exibe os dados atuais do contato
        mostra_dados(nome, telefone, endereço, cidade, uf)
        nome = pede_nome(nome)  #Pede o novo nome (ou mantém o atual)
        telefone = pede_telefone(telefone)  #Pede o novo telefone (ou mantém o atual)
        endereço = pede_endereço(endereço)  #Pede o novo endereço (ou mantém o atual)
        cidade = pede_cidade(cidade)  #Pede a nova cidade (ou mantém a atual)
        uf = pede_uf(uf)  #Pede a nova UF (ou mantém a atual)
        if confirma("alteração") == "S":  #Solicita confirmação para alterar
            agenda[p] = [nome, telefone, endereço, cidade, uf]  #Altera os dados do contato na agenda
            alterada = True  #Marca a agenda como alterada
    else:
        print("Nome não encontrado.")  #Informa que o nome não foi encontrado

#Função para listar todos os contatos da agenda
def lista():
    print("\nAgenda\n\n------")
    for posição, e in enumerate(agenda):  #Percorre a agenda e exibe cada contato
        print(f"Posição: {posição} ", end="")
        mostra_dados(e[0], e[1], e[2], e[3], e[4])
    print("------\n")

#Função para carregar a última agenda gravada
def lê_última_agenda_gravada():
    última = última_agenda()  #Obtém o nome da última agenda gravada
    if última is not None:  #Se houver uma última agenda
        leia_arquivo(última)  #Carrega os dados da agenda do arquivo

#Função para obter o nome da última agenda gravada
def última_agenda():
    try:
        arquivo = open("ultima agenda.dat", "r", encoding="utf-8")
        última = arquivo.readline()[:-1]  #Lê o nome da última agenda do arquivo
        arquivo.close()
    except FileNotFoundError:
        return None  #Retorna None se o arquivo não for encontrado
    return última  #Retorna o nome da última agenda

#Função para atualizar o nome da última agenda gravada
def atualiza_última(nome):
    arquivo = open("ultima agenda.dat", "w", encoding="utf-8")
    arquivo.write(f"{nome}\n")  #Escreve o nome da agenda no arquivo
    arquivo.close()

#Função para ler os dados da agenda de um arquivo
def leia_arquivo(nome_arquivo):
    global agenda, alterada
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            agenda = []  #Limpa a agenda atual
            for l in arquivo.readlines():
                nome, telefone, endereço, cidade, uf = l.strip().split("#")
                agenda.append([nome, telefone, endereço, cidade, uf])  #Adiciona cada contato à agenda
        alterada = False  #Marca a agenda como não alterada
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")  #Informa que o arquivo não foi encontrado
    except IOError:
        print("Erro: Problema ao ler o arquivo.")  #Informa que houve um problema ao ler o arquivo
    except Exception as e:
        print(f"Erro inesperado: {e}")  #Informa que houve um erro inesperado

#Função para carregar uma agenda a partir de um arquivo
def lê():
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação") == "S":
            grava()  #Se houver alterações não salvas, solicita para salvar antes de carregar outra agenda
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)  #Carrega os dados da agenda do arquivo
    atualiza_última(nome_arquivo)  #Atualiza o nome da última agenda carregada

#Função para ordenar os contatos da agenda por nome
def ordena():
    global alterada
    fim = len(agenda)
    while fim > 1:
        i = 0
        trocou = False
        while i < (fim - 1):
            if agenda[i] > agenda[i + 1]:  #Compara os nomes dos contatos e ordena
                temp = agenda[i + 1]
                agenda[i + 1] = agenda[i]
                agenda[i] = temp
                trocou = True
            i += 1
        if not trocou:
            break
    alterada = True  #Marca a agenda como alterada

#Função para gravar a agenda em um arquivo
def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return  #Se não houver alterações, solicita confirmação antes de gravar
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for e in agenda:
                arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}#{e[4]}\n")  #Grava cada contato no arquivo
        atualiza_última(nome_arquivo)  #Atualiza o nome da última agenda gravada
        alterada = False  #Marca a agenda como não alterada
    except IOError:
        print("Erro: Problema ao gravar o arquivo.")  #Informa que houve um problema ao gravar o arquivo
    except Exception as e:
        print(f"Erro inesperado: {e}")  #Informa que houve um erro inesperado

#Função para validar uma entrada de inteiro dentro de uma faixa específica
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))  #Solicita um valor inteiro ao usuário
            if inicio <= valor <= fim:  #Verifica se o valor está dentro da faixa permitida
                return valor  #Retorna o valor se estiver na faixa
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

#Função para exibir o menu principal e obter a opção do usuário
def menu():
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Ordena por nome
0 - Sai
""")
    print(f"\nNomes na agenda: {len(agenda)} Alterada: {alterada}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)  #Retorna a opção escolhida

#Executa a função para carregar a última agenda gravada ao iniciar o programa
lê_última_agenda_gravada()

#Loop principal para exibir o menu e executar as funções conforme a escolha do usuário
while True:
    opção = menu()
    if opção == 0:  #Sai do programa
        break
    elif opção == 1:  #Adiciona um novo contato
        novo()
    elif opção == 2:  #Altera um contato existente
        altera()
    elif opção == 3:  #Apaga um contato existente
        apaga()
    elif opção == 4:  #Lista todos os contatos
        lista()
    elif opção == 5:  #Grava a agenda em um arquivo
        grava()
    elif opção == 6:  #Carrega uma agenda de um arquivo
        lê()
    elif opção == 7:  # Ordena os contatos por nome
        ordena()
