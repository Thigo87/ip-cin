def verTabuleiro(j1, j2): #funcao de teste
    xadrez = []

    for i in range(8):
        nova_linha = []
        for j in range(8):
            nova_linha.append(".")
        xadrez.append(nova_linha)

    for peca in j1:
        for coordenada in j1[peca]:
            xadrez[coordenada[0]][coordenada[1]] = peca

    for peca in j2:
        for coordenada in j2[peca]:
            xadrez[coordenada[0]][coordenada[1]] = peca

    for linha in xadrez:
        print(linha)

def movimentoValido(peca, origem, destino):
    if peca == 'P' and origem[0] == 6 and (destino[0] == 5 or destino[0] == 4) and origem[1] == destino[1]:
        return True
    elif peca == "p" and origem[0] == 1 and (destino[0] == 2 or destino[0] == 3) and origem[1] == destino[1]:
        return True
    else:
        if destino[0] - origem[0] == 1 and origem[1] == destino[1]:
            return True
        else:
            return False

def xadrez(jogador_anterior, rei_capturado, dict_pecas_n, dict_pecas_j):
    jogada = input()
    jogador, origem, destino = jogada.split()

    if jogador == jogador_anterior or rei_capturado:
        if rei_capturado:
            print("Xeque-mate")
        else:
            print("Perdeu por insistencia")
    else:
        xadrez(jogador, False, dict_pecas_n, dict_pecas_j)

pecas_n = {"P":[[6,0],[6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7]],
           "T" : [[7,0], [7,7]], 
           "C" : [[7,1], [7,6]], 
           "B" : [[7,2], [7,5]],
           "D" : [[7,3]],
           "R" : [[7,4]]}

pecas_j = {"p":[[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]],
            "t" : [[0,0], [0,7]], 
            "c" : [[0,1], [0,6]], 
            "b" : [[0,2], [0,5]],
            "d" : [[0,3]],
            "r" : [[0,4]]}

