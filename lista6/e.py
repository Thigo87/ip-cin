def movimentoValido(peca, origem, destino, jogador, dict_jogador):
    if peca.isupper() and jogador == "N":
        if peca == "P": #só falta fazer a captura
            print(dict_jogador[peca][destino[1]])
            if origem[1] == destino[1]:
                print("passou")
                return True
            else:
                return False
        elif peca == "T":
            pass
    elif peca.islower() and jogador == "C":
        pass
    else:
        return False
            
def xadrez(jogador, origem, destino, jogador_anterior, rei_capturado, dict_pecas_n, dict_pecas_j):
    if jogador == jogador_anterior or rei_capturado:
        if rei_capturado:
            print("Xeque-mate")
        else:
            print("Perdeu por insistencia")
    else:
        movimento = input("Digite o destino: ")
        x, y = movimento.split()
        coordenada = [6, 5]
        if movimentoValido("P", coordenada, [int(x), int(y)], jogador, dict_pecas_n):
            nova_coordenada = [int(x), int(y)]
            for peca in dict_pecas_n:
                if coordenada in dict_pecas_n[peca]:
                    print(dict_pecas_n[peca])             
                    dict_pecas_n[peca].pop(coordenada[1])
                    dict_pecas_n[peca].append(nova_coordenada)

            verTabuleiro(dict_pecas_n, dict_pecas_j)

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

verTabuleiro(pecas_n, pecas_j)

xadrez("N", 0, 0, 1, False, pecas_n, pecas_j)