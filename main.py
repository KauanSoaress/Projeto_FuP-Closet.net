# importações
from time import sleep
from datetime import date

# Função home, menu principal
def home():
    # menu inicial
    print("=-=" * 15)
    print(
        '''
    Olá, seja bem vindo ao Closet.net
    Você deseja acessar qual área?

    [1] Peças
    [2] Busca de peças
    [0] Sair
    ''')
    try:
        opcao = int(input('''    Digite sua opção: ''')) # escolha do menu inicial
    except:
        print("=-=" * 15)
        print("A opção selecionada precisa ser um número dentre as opções.")
        sleep(1)
        home()

    if opcao == 1: # menu para opção "peças"
        print("=-=" * 15)
        print(
            '''
    [1] Cadastro de peças
    [2] Remover
    [3] Alterar
    [4] Vender
    [5] Doar
    [0] Voltar ao início
            ''')
        # seleção com tratamento para a opção "peças"
        while True:
            try:
                opcao_cadastro = int(input('''    Digite sua opção: '''))
                if opcao_cadastro in [1, 2, 3, 4, 5, 0]:
                    break
                else:
                    print("=-=" * 15)
                    print("Ops, você selecionou uma opção incorreta, tente novamente")
                    sleep(1)
            except:
                print("=-=" * 15)
                print("A opção selecionada precisa ser um número dentre as opções.")
                sleep(1)

        if opcao_cadastro == 1: # caso em que vai para o cadastro de peças
            # adicionando no arquivo das roupas
            arquivo = open('Roupas.txt', 'a')

            arquivo.write(str(cadastrar()) + '\n') # chamada da função cadastrar

            arquivo.close()

            home()
        elif opcao_cadastro == 2: # caso em que vai para a parte de remoção de peças
            remover_peca()
        elif opcao_cadastro == 3: # caso em que vai para a parte de edição de peças
            editar_roupa()
        elif opcao_cadastro == 4: # caso em que vai para a parte de venda de peças
            vender_peca()
        elif opcao_cadastro == 5: # caso em que vai para a parte de doação de peças
            doar_peca()
        elif opcao_cadastro == 0: # caso em que volta ao início
            print("=-=" * 15)
            sleep(1)

            print('''    Voltando ao início...''')

            sleep(2)

            home()
        else:
            print("Ops, você selecionou uma opção incorreta, tente novamente.")
            sleep(2)

    elif opcao == 2: # caso em que entra no menu de busca
        sleep(1)
        busca()

    elif opcao == 0: # caso que encerra o programa
        print("=-=" * 15)
        sleep(1)

        print('''    Obrigado por usar o Closet.net''')

        sleep(2)
        exit()

    else:
        print("Ops, você selecionou uma opção incorreta, tente novamente.")
        sleep(2)
        home()

# função para recebimento com tratamento da entrada
def receber():
    while True:
        try:
            opcao = int(input('''    Digite sua opção: ''')) # pega o dado do usuário
            if opcao not in [1, 2, 3]: # caso que não é 1, 2 ou 3
                print("Opção inválida, tente novamente.")
                sleep(1)
                print("=-=" * 15)
            else: # caso em que é 1, 2 ou 3, que vai sair do while True
                break
        except:
            print("A entrada precisa ser um número dentre as opções.") # caso em que não é posto um número

    return opcao # retorno da função

# Função para receber entrada para inputs de 3 opções na função editar_roupa
def receber_com_3_itens():
    while True:
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao in [1, 2, 3]:
                break
            else:
                sleep(0.5)
                print("\nOpção inválida.\n")
                sleep(0.5)
        except:
            sleep(0.5)
            print("\nOpção inválida.\n")
            sleep(0.5)

    return opcao

# Função para a remoção de peças do guarda-roupa
def remover_peca():
    # declaração de listas e variável de contador usados
    lista_roupas = transform_str_to_dict()
    lista_ids = []
    cont_roupas = 0

    # for para a listagem de roupas
    for i in lista_roupas:
        lista_ids.append(i['codigo'])
        # condicionais para o tipo da roupa
        if i['tipo'] == 1:
            tipo = "Calçado"
        elif i['tipo'] == 2:
            tipo = "Inferior"
        elif i['tipo'] == 3:
            tipo = "Superior"
        # condicionais para o tamanho da roupa
        if i['tamanho'] == 1:
            tamanho = "P"
        elif i['tamanho'] == 2:
            tamanho = "M"
        elif i['tamanho'] == 3:
            tamanho = "G"
        # condicionais para o padrão da roupa
        if i['padrao'] == 1:
            padrao = "Feminino"
        elif i['padrao'] == 2:
            padrao = "Masculino"
        elif i['padrao'] == 3:
            padrao = "Unissex"
        # condicionais para a situação da roupa
        if i['situacao'] == 1:
            situacao = "Doação"
        elif i['situacao'] == 2:
            situacao = "Venda"
        elif i['situacao'] == 3:
            situacao = "Ficar"

        # exibição dos dados de cada peça
        print("=-=" * 15)
        print("Código da roupa: %s" % (i['codigo']))
        print("Tipo da roupa: %s" % (tipo))
        print("Tamanho da roupa: %s" % (tamanho))
        print("Padrão da roupa: %s" % (padrao))
        print("Cor da roupa: %s" % (i['cor']))
        print("Data de aquisição da roupa: %s" % (i['data_aquisicao']))
        print("Situação da roupa: %s" % (situacao))
        if situacao == 2:
            print("Preço da roupa: %.2f" % (i['preco']))
        print("Estilo da roupa: %s" % (i['estilo']))
        cont_roupas += 1

    if cont_roupas == 0:  # condicional para caso não exista roupas
        print("=-=" * 15)
        print("Não há roupas cadastradas no guarda-roupa.")
        sleep(1)
        home()
    else: # caso em que existem roupas
        print("=-=" * 15)
        print("Essas são as roupas que estão cadastradas no guarda-roupa.")
        while True: # laço para receber o ID da roupa que deseja remover
            print("=-=" * 15)
            id_remover = int(
                input("Digite o ID da roupa que deseja remover: "))
            if id_remover in lista_ids: # verifica se o id selecionado está na lista de ID's
                while True:  # laço para recebimento da confirmação de remoção
                    print("=-=" * 15)
                    escolha = int(input(
                        "Você tem certeza que deseja remover a roupa do id %d? [1-SIM / 0-NÃO] " % id_remover))
                    if escolha == 1:
                        break
                    elif escolha == 0:
                        print("=-=" * 15)
                        print("Ok, tente novamente. ")
                        sleep(1)
                        remover_peca()
                break
            else: # caso em que não tem o ID na lista de ID's
                print("=-=" * 15)
                print("Não temos roupa com esse ID, por favor, digite um ID válido.")
        
        lista_estilos = [] # cria uma lista para por os estilos, para aplicar a remoção da peça também no contador do estilo
        arq_estilos = open('estilos.txt', 'r')
        for i in arq_estilos:
            lista_estilos.append(i.strip()) # adiciona todos os estilos na lista
        arq_estilos.close()
        
        new_lista_estilos = [] # cria uma nova lista para receber os estilos como dicionário
        for i in lista_estilos:
            new_lista_estilos.append(eval(i)) # convertendo para dicionário enquanto adiciona na lista

        # verifica em cada roupa na lista de roupas
        for i in lista_roupas:
            if i['codigo'] == id_remover: # se o ID da roupa for igual ao ID para remoção
                for j in new_lista_estilos: # roda um for na lista com os estilos
                    if i['estilo'] == j['estilo']: # verifica se o estilo da roupa é o mesmo do J
                        j['quant'] -= 1 # se for, diminui 1 do contador
                lista_roupas.remove(i) # remove a roupa da lista de roupas
        
        arq_estilos = open('estilos.txt', 'w')
        for i in new_lista_estilos:
            arq_estilos.write(str(i) + '\n') # reescreve o arquivo de estilos com a alteração
        arq_estilos.close()

        arq_roupas = open('Roupas.txt', 'w')
        for i in lista_roupas:
            arq_roupas.write(str(i) + '\n') # reescreve o arquivo das roupas com a remoção da roupa
        arq_roupas.close()

        print("=-=" * 15)
        sleep(1)
        print("Removendo...")
        sleep(1)
        print("Removido!")
        sleep(1)
        home()

# Função para editar as peças do guarda-roupa
def editar_roupa():
    # declaração de listas e variável de contador usados
    lista_roupas = transform_str_to_dict()
    lista_ids = []
    cont_roupas = 0

    # for para a listagem de roupas
    for i in lista_roupas:
        lista_ids.append(i['codigo'])
        # condicionais para o tipo da roupa
        if i['tipo'] == 1:
            tipo = "Calçado"
        elif i['tipo'] == 2:
            tipo = "Inferior"
        elif i['tipo'] == 3:
            tipo = "Superior"
        # condicionais para o tamanho da roupa
        if i['tamanho'] == 1:
            tamanho = "P"
        elif i['tamanho'] == 2:
            tamanho = "M"
        elif i['tamanho'] == 3:
            tamanho = "G"
        # condicionais para o padrão da roupa
        if i['padrao'] == 1:
            padrao = "Feminino"
        elif i['padrao'] == 2:
            padrao = "Masculino"
        elif i['padrao'] == 3:
            padrao = "Unissex"
        # condicionais para a situação da roupa
        if i['situacao'] == 1:
            situacao = "Doação"
        elif i['situacao'] == 2:
            situacao = "Venda"
        elif i['situacao'] == 3:
            situacao = "Ficar"

        # exibição das informações das Peças
        print("=-=" * 15)
        print("Código da roupa: %s" % (i['codigo']))
        print("Tipo da roupa: %s" % (tipo))
        print("Tamanho da roupa: %s" % (tamanho))
        print("Padrão da roupa: %s" % (padrao))
        print("Cor da roupa: %s" % (i['cor']))
        print("Data de aquisição da roupa: %s" % (i['data_aquisicao']))
        print("Situação da roupa: %s" % (situacao))
        if situacao == 2:
            print("Preço da roupa: %.2f" % (i['preco']))
        cont_roupas += 1

    if cont_roupas == 0:  # condicional para caso não exista roupas
        print("=-=" * 15)
        print("Não há roupas cadastradas no guarda-roupa.")
        sleep(1)
        home()
    else:
        print("=-=" * 15)
        print("Essas são as roupas que estão cadastradas no guarda-roupa.")
        # while True que vai receber o ID desejado, realizando a verificação se está na lista de ID's e realizando a confirmação após
        while True:
            print("=-=" * 15)
            id_editar = int(input("Digite o ID da roupa que deseja editar: "))
            if id_editar in lista_ids:
                while True:
                    print("=-=" * 15)
                    escolha = int(input(
                        "Você tem certeza que deseja editar a roupa do id %d? [1-SIM / 0-NÃO] " % id_editar))
                    if escolha == 1:
                        break
                    elif escolha == 0:
                        print("=-=" * 15)
                        print("Ok, tente novamente. ")
                        sleep(1)
                        editar_roupa()
                break
            else: # caso em que não há foi digitado um ID válido
                print("=-=" * 15)
                print("Não temos roupa com esse ID, por favor, digite um ID válido.")

        for i in lista_roupas: # for para procurar na lista de roupas
            if i['codigo'] == id_editar: # verifica se o ID é igual ao informado pelo usuário
                print("=-=" * 15)
                print('''
    O que você deseja editar?
    [1] Tipo
    [2] Tamanho
    [3] Padrão
    [4] Cor
    [5] Data de Aquisição
    [6] Situação
                ''')
                while True:
                    try:
                        opcao = int(input("Digite a opção desejada: ")) # recebimento do que o usuário deseja editar na peça, com tratamento da entrada para números inválidos
                        if opcao in [1, 2, 3, 4, 5, 6]:
                            break
                        else:
                            print("=-=" * 15)
                            sleep(0.5)
                            print("\nOpção inválida.\n")
                            sleep(0.5)
                    except:
                        print("=-=" * 15)
                        print("\nOpção inválida.\n")


                if opcao == 1:
                    print("=-=" * 15)
                    print('''
    Qual o novo tipo para a roupa?
    [1] Calçado
    [2] Inferior
    [3] Superior
                    ''')
                    novo_tipo = receber_com_3_itens() # recebimento do novo tipo

                    i['tipo'] = novo_tipo

                elif opcao == 2:
                    print("=-=" * 15)
                    print('''
    Qual o novo tamanho para a roupa?
    [1] P
    [2] M
    [3] G
                    ''')
                    novo_tamanho = receber_com_3_itens() # recebimento do novo tamanho

                    i['tamanho'] = novo_tamanho

                elif opcao == 3:
                    print("=-=" * 15)
                    print('''
    Qual o novo tamanho para a roupa?
    [1] Feminino
    [2] Masculino
    [3] Unissex
                    ''')
                    novo_padrao = receber_com_3_itens() # recebimento do novo padrão

                    i['padrao'] = novo_padrao

                elif opcao == 4:
                    print("=-=" * 15)
                    nova_cor = input("Digite a nova cor: ").upper() # recebimento da nova cor

                    i['cor'] = nova_cor

                elif opcao == 5:
                    while True:
                        print("=-=" * 15)
                        nova_data = input("Qual a nova data (dd/mm/aaaa) da roupa? ") # recebimento da nova data
                        try:
                            day = int(nova_data[0:2])
                            mes = int(nova_data[3:5])
                            ano = int(nova_data[6:10])

                            if len(str(ano)) == 4:
                                break
                        except:
                            print("=-=" * 15)
                            print("Por favor, digite a data no padrão informado.")

                    i['data_aquisicao'] = nova_data

                elif opcao == 6:
                    print("=-=" * 15)
                    print('''
    Qual a nova situação para a roupa?
    [1] Doação
    [2] Venda
    [3] Ficar
                    ''')
                    nova_situacao = receber_com_3_itens() # recebimento da nova situação

                    if i['situacao'] == 2 and nova_situacao != 2: # se a situação antiga dor de venda, e a nova não, vai retirar o preço
                        i.pop('preco')

                    i['situacao'] = nova_situacao 

                    if nova_situacao == 2:
                        i['preco'] = float(input("Digite o preço: ")) # se a nova situação for de venda, vai pedir o preço

        arq_roupas = open('Roupas.txt', 'w')
        for i in lista_roupas:
            arq_roupas.write(str(i) + '\n') # reescrevendo a edição no arquivo 
        arq_roupas.close()

        print("=-=" * 15)
        sleep(1)
        print("Editando...")
        sleep(1)
        print("Editado!")
        sleep(1)
        home()

# Função para geração de id's aleatórios
def gerar_id():
    # criação de id automaticamente, com base no último id que tem no arquivo de ids
    arq_id = open("ids.txt", "r")

    # pega o id que tá no arquivo e atribui a variável, somando 1
    codigo_identif = (int(arq_id.readline()) + 1)

    arq_id.close()

    arq_id2 = open("ids.txt", "w")

    # escreve por cima do arquivo, adicionando o novo id, que foi adicionado 1
    arq_id2.write(str(codigo_identif))

    arq_id2.close()

    return codigo_identif

# Função para realizar cadastro de peças roupas
def cadastrar():
    codigo_identif = gerar_id()

    print("=-=" * 15)
    print("Roupa do id %d" % codigo_identif)

    print("=-=" * 15)
    print(
        '''
    Tipo da peça

    [1] Calçado
    [2] Inferior
    [3] Superior
    '''
    )
    tipo = receber()  # recebimento do tipo da roupa

    print("=-=" * 15)
    print(
        '''
    Tamanho da peça

    [1] P
    [2] M
    [3] G
    '''
    )
    tamanho = receber()  # recebimento do tamanho da roupa

    print("=-=" * 15)
    print(
        '''
    Padrão da peça

    [1] Feminino
    [2] Masculino
    [3] Unissex
    '''
    )

    padrao = receber()  # recebimento do padrão da roupa

    print("=-=" * 15)
    cor = input("Qual a cor da roupa? ").upper()  # recebimento da cor da roupa

    # recebimento da data de aquisição da roupa
    while True:
        print("=-=" * 15)
        data_aquisicao = input("Qual a data de aquisição (dd/mm/aaaa) da roupa? ")
        try:
            day = int(data_aquisicao[0:2])
            mes = int(data_aquisicao[3:5])
            ano = int(data_aquisicao[6:10])

            data_atual = date.today() # pega a data atual 
            if day <= 31 and mes <= 12 and ano <= data_atual.year and len(str(ano)) == 4: # condição para sair do while True
                break
        except:
            print("=-=" * 15)
            print("Por favor, digite a data no padrão informado.")

    print("=-=" * 15)
    print(
        '''
    Situação da peça

    [1] Doação
    [2] Venda
    [3] Ficar
    '''
    )
    situacao = receber()  # recebimento da situação da roupa

    if situacao == 2:
        print("=-=" * 15)

        while True:
            try:
                # recebimento do preço da roupa quando a opção for venda
                preco = float(input("Qual o preço da roupa? "))
                break
            except:
                print("O preço da roupa precisa ser um número, tente novamente.")

    print("=-=" * 15)

    estilo = input("Digite o nome do estilo da roupa: ").upper() # recebimento do estilo da roupa

    arq_estilos = open('estilos.txt', 'r')
    estilos = arq_estilos.readlines() # lê cada linha do arquivo de estilos e adiciona numa lista
    arq_estilos.close()

    lista_estilos = []
    for i in estilos:
        lista_estilos.append(i.strip()) # adiciona os estilos sem o \n numa nova lista

    nova_lista_estilos = []
    for i in lista_estilos:
        nova_lista_estilos.append(eval(i)) # converte cada linha para um dicionário e adiciona numa nova lista

    cont_ocorrencias = 0 # contador para guardar a ocorrencia dos estilos

    for i in nova_lista_estilos:
        if estilo in i['estilo']: # se o estilo estiver na lista em algum dos dicionários da lista de estilos, será incrementado 1 no contador
            cont_ocorrencias += 1
            i['quant'] += 1 # se tiver na lista vai ser incrementado 1 no contador dos estilos
            break

    if cont_ocorrencias == 0: # se a quantidade de ocorrencias for diferente de 0 vai ser criado um novo estilo
        nova_lista_estilos.append({'estilo': estilo, 'quant': 1})

    arq_estilos = open('estilos.txt', 'w')
    for i in nova_lista_estilos:
        arq_estilos.write(str(i) + '\n') # a nova lista de estilo vai ser escrito por cima do antigo 
    arq_estilos.close()
    
    print("=-=" * 15)
    sleep(1)

    print("Cadastro da roupa realizado!")

    sleep(1)

    try:  # retornando um dicionário quando é passado o valor do preço
        cadastro = {
            'codigo': codigo_identif,
            'tipo': tipo,
            'tamanho': tamanho,
            'padrao': padrao,
            'cor': cor,
            'data_aquisicao': data_aquisicao,
            'situacao': situacao,
            'preco': preco,
            'estilo': estilo
        }

        return cadastro

    except:  # retornando um dicionário quando não é passado o valor do preço
        cadastro = {
            'codigo': codigo_identif,
            'tipo': tipo,
            'tamanho': tamanho,
            'padrao': padrao,
            'cor': cor,
            'data_aquisicao': data_aquisicao,
            'situacao': situacao,
            'estilo': estilo
        }

        return cadastro

# Função para retornar uma lista com as roupas por ordem decrescente de data
def conferir_datas(list):
    data_atual = date.today() # pega a data atual 
    qt_dias_atual = data_atual.day + (data_atual.month * 30) + (data_atual.year * 365) # calcula a quantidade de dias na data atual

    lista = list
    lista_roupas_qt_dias = []
    lista_qt_dias = []

    for i in lista:
        qt_dias = int(i['data_aquisicao'][0:2]) + (int(i['data_aquisicao'][3:5]) * 30) + (int(i['data_aquisicao'][6:10]) * 365) # calcula a quantidade de dias no dia informado no cadastro da peça

        dias_result = qt_dias_atual - qt_dias # calcula a quantidade de dias, subtraindo a dataatual da do cadastro
        lista_qt_dias.append(dias_result)
        linha = []
        linha.append(dias_result) # adiciona a quantidade de dias a uma linha para por na matriz
        linha.append(i) # adiciona o elemento a uma linha para por na matriz
        lista_roupas_qt_dias.append(linha)

    lista_qt_dias.sort() # ordena as quantidades por ordem crescente

    lista_mais_atuais = []

    for i in lista_qt_dias: # for para buscar os elementos da matriz em que a quantidade de dias corresponde a cada elemento da lista ordenada
        for j in lista_roupas_qt_dias: # for para fazer a comparação
            if j[0] == i: # verifica quando é igual
                lista_mais_atuais.append(j[1]) # então adiciona na lista dos mais atuais a peça com a data mais recente 
                lista_roupas_qt_dias.remove(j) # remove o elemento da lista para não haver perigo de dupla contagem
                break

    return lista_mais_atuais

# Função para retornar uma lista por ordem crescente de perço
def preco_crescente(list):
    precos = []
    for i in list:
        precos.append(i['preco']) # pega os elementos da lista, e adiciona os preços em outra lista separada

    precos.sort() # ordena por ordem crescente os preços

    lista_precos_crescente = []

    for i in precos: # para cada preço vai fazer uma buscar na lista passada na função
        for j in list:
            if j['preco'] == i: # verifica qual tem o preço igual ao que está no primeiro for
                lista_precos_crescente.append(j) # o que tiver é adicionado na nova lista
                list.remove(j) # depois é removido da lista anterior
                break

    return lista_precos_crescente

# Função para encaminhar para o mostrador de peças devido
def mostrar_pecas(sit, tam, pad):
    if sit == 1:
        mostrar_pecas_doacao(tam, pad)
    elif sit == 2:
        mostrar_pecas_venda(tam, pad)
    elif sit == 3:
        mostrar_pecas_ficar(tam, pad)

# Função para mostrar as roupas para doação com base nas especificações do usuário
def mostrar_pecas_doacao(tam, pad):
    lista_roupas = transform_str_to_dict() # pega todas as roupas presentes no guarda-roupa e adiciona numa lista
    lista_doacao = []

    # para cada peça presente no guarda roupa, vai haver a verificação da sua situação, se for igual a 1 (doação) é adicionada na lista de doação
    for i in lista_roupas: 
        if i['situacao'] == 1:
            lista_doacao.append(i)

    # é usada a função conferir_datas para ordenar as roupas por ordem de data
    lista_roupas_doacao = conferir_datas(lista_doacao)

    cont_roupas = 0  # contador para o caso de não haver roupas com base nas especificações

    for i in lista_roupas_doacao:
        # condicionais para o tipo da roupa
        if i['tipo'] == 1:
            tipo = "Calçado"
        elif i['tipo'] == 2:
            tipo = "Inferior"
        elif i['tipo'] == 3:
            tipo = "Superior"
        # condicionais para o tamanho da roupa
        if i['tamanho'] == 1:
            tamanho = "P"
        elif i['tamanho'] == 2:
            tamanho = "M"
        elif i['tamanho'] == 3:
            tamanho = "G"
        # condicionais para o padrão da roupa
        if i['padrao'] == 1:
            padrao = "Feminino"
        elif i['padrao'] == 2:
            padrao = "Masculino"
        elif i['padrao'] == 3:
            padrao = "Unissex"
        #situação da roupa
        situacao = 'Doação'

        # exibição das roupas para doação (com base nas especificações do usuário)
        if i['tamanho'] == tam and i['padrao'] == pad:
            print("=-=" * 15)
            print("Código da roupa: %s" % (i['codigo']))
            print("Tipo da roupa: %s" % (tipo))
            print("Tamanho da roupa: %s" % (tamanho))
            print("Padrão da roupa: %s" % (padrao))
            print("Cor da roupa: %s" % (i['cor']))
            print("Data de aquisição da roupa: %s" % (i['data_aquisicao']))
            print("Situação da roupa: %s" % (situacao))
            cont_roupas += 1

    if cont_roupas == 0:  # condicional para caso não exista roupas com base nas especificações, mostrando uma mensagem
        print("=-=" * 15)
        print("Não temos peças com essas especificações.")
    sleep(2)
    home()

# Função para mostrar as roupas para venda com base nas especificações do usuário
def mostrar_pecas_venda(tam, pad):
    lista_roupas = transform_str_to_dict() # pega todas as roupas presentes no guarda-roupa e adiciona numa lista
    lista_venda = []

    # para cada peça presente no guarda roupa, vai haver a verificação da sua situação, se for igual a 2 (venda) é adicionada na lista de venda
    for i in lista_roupas:
        if i['situacao'] == 2:
            lista_venda.append(i)

    # é usada a função preco_crescente para ordenar as roupas por ordem de preço
    lista_roupas_venda = preco_crescente(lista_venda)

    cont_roupas = 0  # contador para o caso de não haver roupas com base nas especificações

    for i in lista_roupas_venda:
        # condicionais para o tipo da roupa
        if i['tipo'] == 1:
            tipo = "Calçado"
        elif i['tipo'] == 2:
            tipo = "Inferior"
        elif i['tipo'] == 3:
            tipo = "Superior"
        # condicionais para o tamanho da roupa
        if i['tamanho'] == 1:
            tamanho = "P"
        elif i['tamanho'] == 2:
            tamanho = "M"
        elif i['tamanho'] == 3:
            tamanho = "G"
        # condicionais para o padrão da roupa
        if i['padrao'] == 1:
            padrao = "Feminino"
        elif i['padrao'] == 2:
            padrao = "Masculino"
        elif i['padrao'] == 3:
            padrao = "Unissex"
        # situacao da roupa
        situacao = 'Venda'

        # exibição das roupas para venda (com base nas especificações do usuário)
        if i['tamanho'] == tam and i['padrao'] == pad:
            print("=-=" * 15)
            print("Código da roupa: %s" % (i['codigo']))
            print("Tipo da roupa: %s" % (tipo))
            print("Tamanho da roupa: %s" % (tamanho))
            print("Padrão da roupa: %s" % (padrao))
            print("Cor da roupa: %s" % (i['cor']))
            print("Data de aquisição da roupa: %s" % (i['data_aquisicao']))
            print("Situação da roupa: %s" % (situacao))
            print("Preço da roupa: %.2f" % (i['preco']))
            cont_roupas += 1
    if cont_roupas == 0:  # condicional para caso não exista roupas com base nas especificações, mostrando uma mensagem
        print("=-=" * 15)
        print("Não temos peças com essas especificações.")
    sleep(2)
    home()

# Função para mostrar as roupas para ficar com base nas especificações do usuário
def mostrar_pecas_ficar(tam, pad):
    lista_roupas = transform_str_to_dict() # pega todas as roupas presentes no guarda-roupa e adiciona numa lista
    ficar = []

    # para cada peça presente no guarda roupa, vai haver a verificação da sua situação, se for igual a 3 (ficar) é adicionada na lista de ficar
    for i in lista_roupas:
        if i['situacao'] == 3:
            ficar.append(i)

    cont_roupas = 0  # contador para o caso de não haver roupas com base nas especificações

    for i in ficar:
        # condicionais para o tipo da roupa
        if i['tipo'] == 1:
            tipo = "Calçado"
        elif i['tipo'] == 2:
            tipo = "Inferior"
        elif i['tipo'] == 3:
            tipo = "Superior"
        # condicionais para o tamanho da roupa
        if i['tamanho'] == 1:
            tamanho = "P"
        elif i['tamanho'] == 2:
            tamanho = "M"
        elif i['tamanho'] == 3:
            tamanho = "G"
        # condicionais para o padrão da roupa
        if i['padrao'] == 1:
            padrao = "Feminino"
        elif i['padrao'] == 2:
            padrao = "Masculino"
        elif i['padrao'] == 3:
            padrao = "Unissex"
        # situacao da roupa
        situacao = 'Ficar'

        # exibição das roupas para ficar (com base nas especificações do usuário)
        if i['tamanho'] == tam and i['padrao'] == pad:
            print("=-=" * 15)
            print("Código da roupa: %s" % (i['codigo']))
            print("Tipo da roupa: %s" % (tipo))
            print("Tamanho da roupa: %s" % (tamanho))
            print("Padrão da roupa: %s" % (padrao))
            print("Cor da roupa: %s" % (i['cor']))
            print("Data de aquisição da roupa: %s" % (i['data_aquisicao']))
            print("Situação da roupa: %s" % (situacao))
            cont_roupas += 1
    if cont_roupas == 0:  # condicional para caso não exista roupas com base nas especificações, mostrando uma mensagem
        print("=-=" * 15)
        print("Não temos peças com essas especificações.")
    sleep(2)
    home()

# Função para a busca
def busca():
    print("=-=" * 15)
    print(
        '''
    Você deseja buscar pelo que?

    [1] Filtro para Peças
    [2] Filtro por Estilos
    [3] Históricos
    [0] Voltar para home
    ''')
    while True: # while True para recebimento da opção, com tratamento
        try:
            opcao = int(input('''    Digite a sua opção: '''))
            if opcao in [0, 1, 2, 3]:
                break
            else:
                print("=-=" * 15)
                print("Ops, você selecionou uma opção incorreta, tente novamente..")
                sleep(1)
        except:
            print("=-=" * 15)
            print("A opção selecionada precisa ser um número dentre as opções.")
            sleep(1)

    if opcao == 1: # caso Filtro para Peças
        print("=-=" * 15)
        print(
            '''
    Qual situação da roupa que você buscar?

    [1] Doar
    [2] Vender
    [3] Ficar
        ''')
        situacao = receber() # recebimento da situação desejada
        print("=-=" * 15)
        print(
            '''
    Qual tamanho de roupa você busca?

    [1] P
    [2] M
    [3] G
        ''')
        tamanho = receber() # recebimento do tamanho desejado
        print("=-=" * 15)
        print(
            '''
    Qual padrão de roupa você busca?

    [1] Feminino
    [2] Masculino
    [3] Unissex
        ''')
        padrao = receber() # recebimento do padrão desejado 

        mostrar_pecas(situacao, tamanho, padrao) # chamada da função de mostrar peças
    
    elif opcao == 2:  # caso Filtro por Estilos
        print("=-=" * 15)
        print('''
    Qual tipo de busca você deseja realizar?
    [1] Nome do estilo
    [2] Ocorrência do estilo (contador)
    ''')
        while True: # recebimento da opção, com tratamento
            try:
                opcao_estilo = int(input('''     Digite sua opção: '''))
                if opcao_estilo in [1, 2]:
                    break
                else:
                    print("O valor digitado precisa ser um número válido.")
            except:
                print("O valor digitado precisa ser um número válido.")

        if opcao_estilo == 1: # caso em que é pra listar por nome do estilo
            listar_estilo_por_nome()
        elif opcao_estilo == 2: # caso em que é pra listar pelo contador do estilo
            listar_estilo_por_contador()

    elif opcao == 3: # caso Históricos
        print("=-=" * 15)
        print('''
    Qual histórico você quer ver?
    [1] Doadas
    [2] Vendidas
    ''')
        while True: # recebimento da opção, com tratamento
            try:
                opcao_historico = int(input('''     Digite sua opção: '''))
                if opcao_historico in [1, 2]:
                    break
                else:
                    print("=-=" * 15)
                    print("O valor digitado precisa ser um número válido.")
            except:
                print("=-=" * 15)
                print("O valor digitado precisa ser um número válido.")

        if opcao_historico == 1: # caso histórico das doadas
            listar_doadas()
        elif opcao_historico == 2: # caso histórico das vendidas
            listar_vendidas()

    elif opcao == 0: # caso voltar para tela inicial
        print("=-=" * 15)
        print("Voltando para a home.")
        sleep(1)
        home()

# Função para pegar as linhas do arquivo e transformar em dicionário novamente
def transform_str_to_dict():
    arq = open('Roupas.txt', 'r')  # abre o arquivo pra leitura
    # adiciona todas as linhas em uma lista, cada uma se tornando uma string
    roupas = arq.readlines()
    arq.close()  # fechamento do arquivo
    roupas_list = []
    for i in roupas:
        # adiciona cada linha em uma nova lista, mas sem o \n
        roupas_list.append(i.strip())

    roupas_dict_list = []
    for i in roupas_list:
        # adiciona cada linha em uma nova lista, convertendo para dicionário
        roupas_dict_list.append(eval(i))

    return roupas_dict_list  # retorno da lista de dicionários

# Função para venda de peças
def vender_peca():
    lista_roupas = transform_str_to_dict() # recebimento das peças disponíveis no guarda-roupa
    lista_venda = []
    lista_ids = []

    for i in lista_roupas:
        if i['situacao'] == 2:
            lista_venda.append(i) # pegando somente as roupas disponíveis para venda e guardando em uma lista

    if len(lista_venda) == 0: # se a quantidade de itens na lista de venda for igual a 0, volta pra página inicial
        print("=-=" * 15)
        print("Não temos peças disponíveis para venda.")
        sleep(1)
        home()
    else:
        while True: # recebimento da confirmação, se deseja realizar a venda de alguma peça, com tratamento
            try:
                print("=-=" * 15)
                confirmacao_venda = int(input("Você deseja realizar a venda de alguma peça? [1-SIM / 0-NÃO] "))
                if confirmacao_venda in [0, 1]:
                    break
                else:
                    print("=-=" * 15)
                    print("Número inválido, tente novamente.")
            except:
                print("=-=" * 15)
                print("O valor inserido precisa ser um número dentre as opções.")

        if confirmacao_venda == 0: # se a confirmação for 0, volta para a página inicial
            print("=-=" * 15)
            print("Voltando para home...")
            sleep(1)
            home()

        elif confirmacao_venda == 1: # se for 1, vão ser listadas as roupas disponíveis
            for i in lista_venda:
                lista_ids.append(i['codigo']) # adicionando os ID's das roupas para venda em uma lista de ID's
                # condicionais para o tipo da roupa
                if i['tipo'] == 1:
                    tipo = "Calçado"
                elif i['tipo'] == 2:
                    tipo = "Inferior"
                elif i['tipo'] == 3:
                    tipo = "Superior"
                # condicionais para o tamanho da roupa
                if i['tamanho'] == 1:
                    tamanho = "P"
                elif i['tamanho'] == 2:
                    tamanho = "M"
                elif i['tamanho'] == 3:
                    tamanho = "G"
                # condicionais para o padrão da roupa
                if i['padrao'] == 1:
                    padrao = "Feminino"
                elif i['padrao'] == 2:
                    padrao = "Masculino"
                elif i['padrao'] == 3:
                    padrao = "Unissex"
                # situacao da roupa
                situacao = 'Venda'

                # exibição das peças disponíveis para venda
                print("=-=" * 15)
                print("Código da roupa: %s" % (i['codigo']))
                print("Tipo da roupa: %s" % (tipo))
                print("Tamanho da roupa: %s" % (tamanho))
                print("Padrão da roupa: %s" % (padrao))
                print("Cor da roupa: %s" % (i['cor']))
                print("Data de aquisição da roupa: %s" % (i['data_aquisicao']))
                print("Situação da roupa: %s" % (situacao))
                print("Preço da roupa: %.2f" % (i['preco']))

                while True: # recebimento da peça que se deseja vender (sendo identificada pelo ID)
                    try:
                        print("=-=" * 15)
                        roupa_venda_id = int(
                            input("Digite o código da roupa que você deseja comprar: "))
                        if roupa_venda_id in lista_ids: # checagem se o código informado está na lista de ID's
                            break
                        else: # se não tiver entre os ID's da lista
                            print("=-=" * 15)
                            print(
                                "O ID digitado não corresponde ao de nenhuma roupa, tente novamente.")
                    except:
                        print("=-=" * 15)
                        print("O valor inserido precisa ser um número inteiro.")

                while True: # receimento da confirmação de compra, com tratamento 
                    try:
                        print("=-=" * 15)
                        confirmacao = int(
                            input("Confirma a compra da roupa? [1-SIM / 0-NÃO] "))
                        if confirmacao in [0, 1]:
                            break
                        else:
                            print("=-=" * 15)
                            print(
                                "O ID digitado não corresponde ao de nenhuma roupa, tente novamente.")
                    except:
                        print("=-=" * 15)
                        print("O valor inserido precisa ser um número dentre as opções.")

                if confirmacao == 0: # se a confirmação for 0, volta para a home
                    print("=-=" * 15)
                    print("Voltando para a home...")
                    sleep(1)
                    home()
                else: # se a confirmação for 1...
                    nome = input("Digite o nome do comprador: ") # recebimento do nome do comprador
                    
                    for i in lista_roupas: # verifica todas as roupas da lista de roupas
                        if i['codigo'] == roupa_venda_id: # se o código da roupa for igua ao código da roupa que vai ser vendida...
                            linha = []
                            linha.append(i['preco']) # adiciona numa linha o preço da roupa que foi vendida
                            linha.append(nome) # adiciona o nome do comprador 
                            linha.append(i) # e adiciona a peça vendida

                            arq_vendas = open("historicos/vendidos.txt", "a")
                            arq_vendas.write(str(linha) + "\n") # adiciona a linha no arquivo das roupas vendidas 
                            arq_vendas.close()

                            lista_roupas.remove(i) # remove a roupa vendida da lista de roupas

                            arq_roupas = open("roupas.txt", "w")
                            for i in lista_roupas:
                                arq_roupas.write(str(i) + "\n") # reescreve cada linha da lista em uma linha do arquivo, atualizando ele após a remoção da roupa
                            arq_roupas.close()

                            print("=-=" * 15)
                            print("Processando venda...")
                            sleep(1)
                            print("Venda computada!")
                            sleep(1)
                            home()

# Função para doação de peças
def doar_peca():
    lista_roupas = transform_str_to_dict() # recebimento das peças disponíveis no guarda-roupa
    lista_doacao = []
    lista_ids = []

    for i in lista_roupas:
        if i['situacao'] == 1:
            lista_doacao.append(i) # pegando somente as roupas disponíveis para doação e guardando em uma lista

    if len(lista_doacao) == 0: # se a quantidade de itens na lista de doação for igual a 0, volta pra página inicial
        print("=-=" * 15)
        print("Não temos peças disponíveis para doação.")
        sleep(1)
        home()
    
    else:
        while True: # recebimento da confirmação, se deseja realizar a doação de alguma peça, com tratamento
            try:
                print("=-=" * 15)
                confirmacao_doacao = int(
                    input("Você deseja realizar a doação de alguma peça? [1-SIM / 0-NÃO] "))
                if confirmacao_doacao in [0, 1]:
                    break
                else:
                    print("=-=" * 15)
                    print("Número inválido, tente novamente.")
            except:
                print("=-=" * 15)
                print("O valor inserido precisa ser um número dentre as opções.")

        if confirmacao_doacao == 0: # se a confirmação for 0, volta para a página inicial
            print("=-=" * 15)
            print("voltando para home")
            sleep(1)
            home()
        elif confirmacao_doacao == 1:  # se for 1, vão ser listadas as roupas disponíveis

            for i in lista_doacao:
                lista_ids.append(i['codigo']) # adicionando os ID's das roupas para venda em uma lista de ID's
                # condicionais para o tipo da roupa
                if i['tipo'] == 1:
                    tipo = "Calçado"
                elif i['tipo'] == 2:
                    tipo = "Inferior"
                elif i['tipo'] == 3:
                    tipo = "Superior"
                # condicionais para o tamanho da roupa
                if i['tamanho'] == 1:
                    tamanho = "P"
                elif i['tamanho'] == 2:
                    tamanho = "M"
                elif i['tamanho'] == 3:
                    tamanho = "G"
                # condicionais para o padrão da roupa
                if i['padrao'] == 1:
                    padrao = "Feminino"
                elif i['padrao'] == 2:
                    padrao = "Masculino"
                elif i['padrao'] == 3:
                    padrao = "Unissex"
                # situacao da roupa
                situacao = 'Doacao'

                # exibição das peças disponíveis
                print("=-=" * 15)
                print("Código da roupa: %s" % (i['codigo']))
                print("Tipo da roupa: %s" % (tipo))
                print("Tamanho da roupa: %s" % (tamanho))
                print("Padrão da roupa: %s" % (padrao))
                print("Cor da roupa: %s" % (i['cor']))
                print("Data de aquisição da roupa: %s" % (i['data_aquisicao']))
                print("Situação da roupa: %s" % (situacao))

            while True: # recebimento do ID da peça que será doada
                try:
                    print("=-=" * 15)
                    roupa_doacao_id = int(
                        input("Digite o código da roupa que você deseja doar: "))
                    if roupa_doacao_id in lista_ids: # verificação se o ID está na lista de ID's
                        break
                    else:
                        print("=-=" * 15)
                        print(
                            "O ID digitado não corresponde ao de nenhuma roupa, tente novamente.")
                except:
                    print("=-=" * 15)
                    print("O valor inserido precisa ser um número inteiro.")
            # recebimento da confirmação de doação 
            while True:
                try:
                    print("=-=" * 15)
                    confirmacao = int(
                        input("Confirma a doação da roupa? [1-SIM / 0-NÃO] "))
                    if confirmacao in [0, 1]:
                        break
                    else:
                        print("=-=" * 15)
                        print(
                            "O ID digitado não corresponde ao de nenhuma roupa, tente novamente.")
                except:
                    print("=-=" * 15)
                    print("O valor inserido precisa ser um número dentre as opções.")

            if confirmacao == 0: # se a confirmação for 0, volta para a home
                print("=-=" * 15)
                print("Voltando para home...")
                sleep(1)
                home()
            else: # se a confirmação for 1
                for i in lista_roupas: # procura em todas as roupas da lista de roupas
                    if i['codigo'] == roupa_doacao_id: # quando o ID da roupa for igual ao ID informado pelo usuário
                        linha = []
                        print("=-=" * 15)
                        linha.append(input("Digite a ONG/Pessoa que a peça será doada: ")) # recebimento da ONG/Pessoa para quem vai ser doada, já adicionando numa lista
                        linha.append(i) # adicionando também a peça doada na lista

                        arq_doacao = open("historicos/doadas.txt", "a")
                        arq_doacao.write(str(linha) + "\n") # adicionando a peça na lista de roupas
                        arq_doacao.close()

                        lista_roupas.remove(i) # removendo a peça da lista de roupas

                        arq_roupas = open("roupas.txt", "w")
                        for i in lista_roupas:
                            arq_roupas.write(str(i) + "\n") # reescrevendo a lista de roupas, agora sem a roupa que foi doada
                        arq_roupas.close()

                        print("=-=" * 15)
                        print("Processando doação...")
                        sleep(1)
                        print("Doação computada!")
                        sleep(1)
                        home()

# Função para listar os estilos por nome, mostrando as peças presentes no estilo
def listar_estilo_por_nome():
    lista_estilos = []
    arq = open('estilos.txt', 'r')
    for i in arq:
        lista_estilos.append(i) # lista as linhas no arquivo dos estilos e adiciona numa lista
    arq.close()

    for i in lista_estilos:
        i.strip() # remove os \n de cada linha
    
    new_lista_estilos = []
    for i in lista_estilos:
        new_lista_estilos.append(eval(i)) # adiciona numa nova lista, convertendo para dicionário 

    if len(new_lista_estilos) == 0:  # caso que não há estilos cadastrados
        print("=-=" * 15)
        print('''   ---Não há estilos cadastrados---''')
        sleep(1)
        home()
    else:
        print("=-=" * 15)
        print("Esses são os estilos que estão cadastrados: ")
        for i in new_lista_estilos:
            print(i['estilo']) # print dos estilos presentes

        nomes_estilos = []
        for i in new_lista_estilos:
            nomes_estilos.append(i['estilo']) # adicionando os nomes dos estilos em uma lista
        
        while True: # recebiment odo estilo desejado, com tratamento para caso não digite corretamente
            print("=-=" * 15)
            estilo_selecao = input("Digite o estilo que você deseja: ").upper()
            if estilo_selecao in nomes_estilos: # verificação se o nome digitado está na lista
                break
            else:
                print("=-=" * 15)
                print("O nome informado não se encontra na nossa lista de estilos, tente novamente. ")

        while True: # confirmação de certeza em relação ao estilo selecionado 
            try:
                print("=-=" * 15)
                confirmacao = int(input("Tem certeza em relação ao estilo selecionado? [1-SIM / 0-NÃO] "))
                if confirmacao in [1, 0]:
                    break
                else:
                    print("=-=" * 15)
                    print("Digite um número válido.")
            except:
                print("=-=" * 15)
                print("Digite um número válido.")

        if confirmacao == 1: # se a confirmação for sim
            lista_roupas = []
            arq_roupas = open('Roupas.txt', 'r')
            for i in arq_roupas:
                lista_roupas.append(i) # recebendo as roupas do guarda-roupa e adicionando numa lista
            arq_roupas.close()

            for i in lista_roupas:
                i.strip() # tirando os \n de cada elemento 
            
            new_lista_roupas = []
            for i in lista_roupas:
                new_lista_roupas.append(eval(i)) # transformando cada elemento em um dicionário 

            lista_roupas_selecionadas = []
            for i in new_lista_estilos: # verifica os estilos cadastrados
                if estilo_selecao == i['estilo']: # procura o estilo da lista de estilos que é igual ao digitado pelo usuário 
                    for j in new_lista_roupas: # quando achar, vai passar por todos os elementos da lista de roupas
                        if j['estilo'] == estilo_selecao: # verifica se o estilo da roupa é igual estilo informado 
                            lista_roupas_selecionadas.append(j) # se for igual a roupa é adicionada a lista

            cont_roupas = 0
            for i in lista_roupas_selecionadas: # pega todas as roupas selecionadas 
                # condicionais para o tipo da roupa
                if i['tipo'] == 1:
                    tipo = "Calçado"
                elif i['tipo'] == 2:
                    tipo = "Inferior"
                elif i['tipo'] == 3:
                    tipo = "Superior"
                # condicionais para o tamanho da roupa
                if i['tamanho'] == 1:
                    tamanho = "P"
                elif i['tamanho'] == 2:
                    tamanho = "M"
                elif i['tamanho'] == 3:
                    tamanho = "G"
                # condicionais para o padrão da roupa
                if i['padrao'] == 1:
                    padrao = "Feminino"
                elif i['padrao'] == 2:
                    padrao = "Masculino"
                elif i['padrao'] == 3:
                    padrao = "Unissex"
                # situacao da roupa
                if i['situacao'] == 1:
                    situacao = "Doação"
                elif i['situacao'] == 2:
                    situacao = 'Venda'
                elif i['situacao'] == 3:
                    situacao = 'Ficar'

                # exibição das roupas
                print("=-=" * 15)
                print("Código da roupa: %s" % (i['codigo']))
                print("Tipo da roupa: %s" % (tipo))
                print("Tamanho da roupa: %s" % (tamanho))
                print("Padrão da roupa: %s" % (padrao))
                print("Cor da roupa: %s" % (i['cor']))
                print("Data de aquisição da roupa: %s" % (i['data_aquisicao']))
                print("Situação da roupa: %s" % (situacao))
                if situacao == 2:
                    print("Preço da roupa: %.2f" % (i['preco']))
                cont_roupas += 1

            if cont_roupas == 0: # caso em que o estilo não tem roupas cadastradas
                print("=-=" * 15)
                print("Esse estilo não tem roupas cadastradas! ")
        else: # caso em que a confirmação é 0, que volta para o início da função
            listar_estilo_por_nome()

        sleep(2)
        home()

# Função para listar os estilos por contador
def listar_estilo_por_contador():
    lista_estilos = []
    arq = open('estilos.txt', 'r')
    for i in arq:
        lista_estilos.append(i) # pega todos os estilos e adiciona em uma lista
    arq.close()

    if len(lista_estilos) == 0: # caso que não há estilos cadastrados
        print("=-=" * 15)
        print('''   ---Não há estilos cadastrados---''')
        sleep(1)
        home()
    else:
        for i in lista_estilos:
            i.strip() # tira o \n de cada elemento 
        
        new_lista_estilos = []
        for i in lista_estilos:
            new_lista_estilos.append(eval(i)) # adiciona os elementos em uma nova lista, transformando em dicionário

        quantidades = []
        for i in new_lista_estilos:
            quantidades.append(i['quant']) # pega as quantidades de cada estilo e adiciona em uma lista

        quantidades.sort() # deixa as quantidade em ordem crescente

        lista_estilo_crescente = []
        for i in quantidades: # for que passa por cada elemento da lista de quantidades 
            for j in new_lista_estilos: # lista os estilos cadastrados
                if j['quant'] == i:  # verifica se a quantidade presente no estilo é igual a quantidade da lista
                    lista_estilo_crescente.append(j) # se for igual, o estilo é adicionado a lista que classifica por ordem crescente
                    new_lista_estilos.remove(j) # remove o estilo da nova lista de estilos para não haver supla contagem 
                    break
        
        for i in lista_estilo_crescente: # for para a exibição dos estilos pela ordem crescente do contador
            print("=-=" * 15)
            # exibição do estilo e do valor do seu contador
            print("Nome do estilo: %s" %i['estilo'])
            print("Quantidade de peças: %s" %i['quant'])
        
        sleep(2)
        home()

# Função para mostrar as peças doadas
def listar_doadas():
    arq = open('historicos/doadas.txt', 'r')
    lista_doadas = []
    for i in arq:
        lista_doadas.append(i) # lista todas as roupas do arquivo das doadas e adiciona em uma lista
    arq.close()

    new_lista_doadas = []
    for i in lista_doadas:
        new_lista_doadas.append(eval(i.strip())) # adiciona numa nova lista, tirando o \n e convertendo para lista 

    if len(new_lista_doadas) == 0:  # caso em que o arquivo com as peças doadas está vazio
        print("=-=" * 15)
        print('''    ---Sem peças doadas---''')
        sleep(1)
        home()
    else:
        print("=-=" * 15)
        print('''
        Listagem das peças doadas: 
        ''')
        for i in new_lista_doadas: # for para exibir as peças doadas
            # condicionais para o tipo da roupa
            if i[1]['tipo'] == 1:
                tipo = "Calçado"
            elif i[1]['tipo'] == 2:
                tipo = "Inferior"
            elif i[1]['tipo'] == 3:
                tipo = "Superior"
            # condicionais para o tamanho da roupa
            if i[1]['tamanho'] == 1:
                tamanho = "P"
            elif i[1]['tamanho'] == 2:
                tamanho = "M"
            elif i[1]['tamanho'] == 3:
                tamanho = "G"
            # condicionais para o padrão da roupa
            if i[1]['padrao'] == 1:
                padrao = "Feminino"
            elif i[1]['padrao'] == 2:
                padrao = "Masculino"
            elif i[1]['padrao'] == 3:
                padrao = "Unissex"

            # exibição das peças doadas
            print("=-=" * 15)
            print("ONG/Pessoa para quem foi doada: %s" %i[0])
            print("Código da roupa: %s" % (i[1]['codigo']))
            print("Tipo da roupa: %s" % (tipo))
            print("Tamanho da roupa: %s" % (tamanho))
            print("Padrão da roupa: %s" % (padrao))
            print("Cor da roupa: %s" % (i[1]['cor']))
            print("Data de aquisição da roupa: %s" % (i[1]['data_aquisicao']))
        
        sleep(1)
        home()

# Função para listar as peças vendidas
def listar_vendidas():
    arq = open('historicos/vendidos.txt', 'r')
    lista_vendidas = []
    for i in arq:
        lista_vendidas.append(i) # pega todas as peças do arquivo das vendidas e adiciona numa lista
    arq.close()

    nova_lista_vendidas = []
    for i in lista_vendidas:
        nova_lista_vendidas.append(eval(i.strip())) # adiciona em uma nova lista, tirando o \n e transformando em lista

    if len(nova_lista_vendidas) == 0: # caso em que o arquivo com as peças vendidas está vazio
        print("=-=" * 15)
        print('''    ---Sem peças vendidas---''')
        sleep(1)
        home()
    else:
        print("=-=" * 15)
        print('''
        Listagem das peças vendidas: 
        ''')
        for i in nova_lista_vendidas: # for para exibir as peças vendidas

            # condicionais para o tipo da roupa
            if i[2]['tipo'] == 1:
                tipo = "Calçado"
            elif i[2]['tipo'] == 2:
                tipo = "Inferior"
            elif i[2]['tipo'] == 3:
                tipo = "Superior"
            # condicionais para o tamanho da roupa
            if i[2]['tamanho'] == 1:
                tamanho = "P"
            elif i[2]['tamanho'] == 2:
                tamanho = "M"
            elif i[2]['tamanho'] == 3:
                tamanho = "G"
            # condicionais para o padrão da roupa
            if i[2]['padrao'] == 1:
                padrao = "Feminino"
            elif i[2]['padrao'] == 2:
                padrao = "Masculino"
            elif i[2]['padrao'] == 3:
                padrao = "Unissex"

            # exibição das peças vendidas
            print("=-=" * 15)
            print("Nome do comprador: %s" %(i[1]))
            print("Código da roupa: %s" % (i[2]['codigo']))
            print("Tipo da roupa: %s" % (tipo))
            print("Tamanho da roupa: %s" % (tamanho))
            print("Padrão da roupa: %s" % (padrao))
            print("Cor da roupa: %s" % (i[2]['cor']))
            print("Data de aquisição da roupa: %s" % (i[2]['data_aquisicao']))
            print("Preço a que foi vendida: %.2f " % (i[2]['preco']))

        sleep(2)
        home()

home()