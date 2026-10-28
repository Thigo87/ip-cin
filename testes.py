def movimentacao(mapa, posicao_atual): #função para movimentação pelo mapa
    maior_valor = 0
    proxima_posicao = [0, 0]
    x, y = posicao_atual[0], posicao_atual[1] #separando as coordenadas

    limites = len(mapa[0]) #definindo os limites do mapa

    if 1 <= x:
        if mapa[x - 1][y] > maior_valor:
            maior_valor = mapa[x - 1][y]
            proxima_posicao = [x - 1, y]
    if limites - 1 > x:
        if mapa[x + 1][y] > maior_valor:
                    maior_valor = mapa[x + 1][y]
                    proxima_posicao = [x + 1, y]

    if 1 <= y:
            if mapa[x][y - 1] > maior_valor:
                maior_valor = mapa[x][y - 1]
                proxima_posicao = [x, y - 1]
    if limites - 1 > y:
        if mapa[x][y + 1] > maior_valor:
                    maior_valor = mapa[x][y + 1]
                    proxima_posicao = [x, y + 1]
    

    return proxima_posicao, maior_valor

posicao_atual = [0, 0]

valor_posicao = 0
mapa = [[0, 8], [4, 99]]

while valor_posicao != 99:
      print(posicao_atual)
      posicao_atual, valor_posicao = movimentacao(mapa, posicao_atual)

print(posicao_atual)