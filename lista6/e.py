def verMapa(tabuleiro):
    mapa = []

    for i in range(8):
        nova_linha = []
        for i in range(8):
            nova_linha.append(".")
        mapa.append(nova_linha)

    for jogador in tabuleiro:
        for peca in tabuleiro[jogador]:
            for coordenada in tabuleiro[jogador][peca]:
                i = coordenada[0]
                j = coordenada[1]
                mapa[i][j] = peca

    for linha in mapa:
        print(linha)

def movimentar(tabuleiro, jogador, origem, destino): #essa função vai retornar o tabuleiro atualizado com as peças devidamente movimentadas
    for player in tabuleiro:
        if player == jogador: 
            for peca in tabuleiro[jogador]:
                for coordenada in tabuleiro[jogador][peca]:
                    if coordenada == origem:
                        tabuleiro[jogador][peca].remove(coordenada)
                        tabuleiro[jogador][peca].append(destino)

    return tabuleiro

def movimentoValido(tabuleiro, peca, origem, destino): #função para verificar se o movimento é válido
    elemento_no_destino = "."

    #criar um if para verificar se o movimento ocorreu dentro do tabuleiro

    if (0 < origem[0] < 8) and (0 < origem[1] < 8) and (0 < destino[0] < 8) and (0 < destino[1] < 8):
        #verificando se o destino está vazio ou há alguma peça
        for player in tabuleiro:
            for item in tabuleiro[player]:
                for coordenada in tabuleiro[player][item]:
                    if coordenada == destino:
                        elemento_no_destino = item

        print(elemento_no_destino)

        if peca == "P" and (elemento_no_destino.islower() or elemento_no_destino == "."):
            if destino[1] == origem[1]:
                if origem[0] == 6 and (destino[0] == 5 or destino[0] == 4): #movimento do inicio
                    return True
                if destino[0] == origem[0] - 1:
                    return True
                else:
                    return False

            #captura
            elif (destino[0] == (origem[0] - 1) and ((destino[1] == origem[1] + 1) or (destino[1] == origem[1] - 1))) and elemento_no_destino.islower():
                return True
                    
            return False
        
        elif peca == "p" and (elemento_no_destino.isupper() or elemento_no_destino == "."):
            if destino[1] == origem[1]:
                if origem[0] == 1 and (destino[0] == 2 or destino[0] == 3): #movimento do inicio
                    return True
                if destino[0] == origem[0] + 1:
                    return True
                else:
                    return False

            #captura    
            elif (destino[0] == (origem[0] + 1) and ((destino[1] == origem[1] + 1) or (destino[1] == origem[1] - 1))) and elemento_no_destino.isupper():
                return True
                    
            return False
        
        elif peca == "T" and (elemento_no_destino.islower() or elemento_no_destino == "."):
            pass
        elif peca == "t" and (elemento_no_destino.isupper() or elemento_no_destino == "."):
            pass
        elif peca == "C" and (elemento_no_destino.islower() or elemento_no_destino == "."):
            pass
        elif peca == "c" and (elemento_no_destino.isupper() or elemento_no_destino == "."):
            pass
        elif peca == "B" and (elemento_no_destino.islower() or elemento_no_destino == "."):
            pass
        elif peca == "b" and (elemento_no_destino.isupper() or elemento_no_destino == "."):
            pass
        elif peca == "D" and (elemento_no_destino.islower() or elemento_no_destino == "."):
            pass
        elif peca == "d" and (elemento_no_destino.isupper() or elemento_no_destino == "."):
            pass
        elif peca == "R" and (elemento_no_destino.islower() or elemento_no_destino == "."):
            pass
        elif peca == "r" and (elemento_no_destino.isupper() or elemento_no_destino == "."):
            pass

    else:
        return False

tabuleiro = {
    "N": {
        "T": [[7, 0], [7, 7]],
        "C": [[7, 1], [7, 6]],
        "B": [[7, 2], [7, 5]],
        "D": [[7, 3]],
        "R": [[7, 4]],
        "P": [[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7]],
    },
    "C": {
        "t": [[0, 0], [0, 7]],
        "c": [[0, 1], [0, 6]],
        "b": [[0, 2], [0, 5]],
        "d": [[0, 3]],
        "r": [[0, 4]],
        "p": [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]],
    },
}


verMapa(tabuleiro)

tabuleiro_novo = movimentar(tabuleiro, "N", [6, 2], [5, 2])
print('\n')
verMapa(tabuleiro_novo)
print(movimentoValido(tabuleiro, "p", [1,4], [2, 5]))