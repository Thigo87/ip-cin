def filtro(mao):
    copia_mao = ['x']
    for carta in mao:
        copia_mao.append(carta)
    
    tamanho = len(copia_mao)
    lista_filtrada = []
    indice_erros = []
    for i in range(1, tamanho//2):
        if copia_mao[i] < copia_mao[2*i]:
            indice_erros.append(2*i)
        if copia_mao[i] < copia_mao[(2*i) + 1]:
            indice_erros.append((2*i) + 1)
    
    for i in range(1, tamanho):
        if i not in indice_erros:
            lista_filtrada.append(copia_mao[i])
    
    return lista_filtrada, len(indice_erros)

def calculo_base(mao, inventario):
    _, erros = filtro(mao) #Quero receber somente a quantidade de erros
    chips = 0
    multiplicador_base = 0
    
    if "Chicot" in inventario:
        erros -= 2
    
    if erros == 0: #Full House
        chips = 40
        multiplicador_base = 4
    elif erros == 1: #Três do mesmo
        chips = 30
        multiplicador_base = 3
    elif erros == 2: #Dois pares
        chips = 20
        multiplicador_base = 2
    else: #Carta Maior
        chips = 5
        multiplicador_base = 1
    
    return chips, multiplicador_base

def separacao_cartas(inventario):
    curingas_base = ['Joker', 'Space Joker', 'Blueprint']   
    arcanos_base = ['Tolo', 'Hierofante', 'Justiça', 'Força']
    
    curingas_presentes = []
    arcanos_presentes = []
    for item in inventario:
        if item in curingas_base:
            curingas_presentes.append(item)
        elif item in arcanos_base:
            arcanos_presentes.append(item)

    return curingas_presentes, arcanos_presentes

def curinga(inventario, chips, multiplicador):
    curingas, _ = separacao_cartas(inventario) #selecionando apenas os curingas
    for i in range(len(curingas)):
        if curingas[i] == "Joker":
            multiplicador += 4
        elif curingas[i] == "Space Joker":
            chips += 20
            multiplicador += 1
        elif curingas[i] == "Blueprint":
            if i < len(curingas):
                if curingas[i + 1] == "Joker":
                    multiplicador += 4
                elif curingas[i + 1] == "Space Joker":
                    chips += 20
                    multiplicador += 1

    return chips, multiplicador

def arcano(inventario, mao, multiplicador):
    _, arcanos_atualizados = separacao_cartas(inventario) #separando os arcanos
    if arcanos_atualizados[0] == "Tolo":
        arcanos_atualizados.pop(0)
        novo_arcano = input()
        arcanos_atualizados.append(novo_arcano)
    elif arcanos_atualizados[0] == "Hierofante":
        arcanos_atualizados.pop(0)
        for i in range(0, len(mao)):
            if mao[i] < 30:
                mao[i] *= 2
    elif arcanos_atualizados[0] == "Justiça":
        arcanos_atualizados.pop(0)
        for i in range(0, len(mao)):
            if mao[i] % 3 == 0:
                multiplicador *= 1.1
    elif arcanos_atualizados[0] == "Força":
        arcanos_atualizados.pop(0)
        for i in range(0, len(mao)):
            if int(mao[i] ** 0.5 ) == mao[i] ** 0.5: #verificação dos quadrados perfeitos
                multiplicador *= 1.1
    
    return multiplicador, mao

def pontuacao(mao, inventario):
    chips, multiplicador_base = calculo_base(mao, inventario)
    chips_atualizados, multiplicador, arcanos = curinga(inventario, chips, multiplicador_base)
    multiplicador, mao = arcano(arcanos, mao, multiplicador)
    
    soma_valores = 0
    for carta in mao:
        soma += carta
        
    chips_totais = chips_atualizados + soma_valores
    
    pontuacao_final = int(chips_totais * round(multiplicador, 2))
    
    return pontuacao_final
    

def rodada(inventario):
    mao = input()
    acao_jogador = input()
    if acao_jogador == "Jogar":
        pass
    elif acao_jogador == "Trocar":
        pass
    elif acao_jogador == "Arcano":
        pass
    
    

meta = int(input())
print(f"Jimbo: Certo, você tem que conseguir {meta} chips. Boa sorte!")
inventario = input()
lista_inventario = inventario.replace("[", "]").replace("]", "").replace("'", "").split(", ")
curingas, arcanos = separacao_cartas(lista_inventario)


rodada(lista_inventario)
