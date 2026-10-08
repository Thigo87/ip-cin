mapa = [[1,2,3],[4,5,6],[7,8,9]]
novo_mapa = []
for i in mapa:
    print(i)

novo_mapa = []

print("")

for i in range(len(mapa)):
    nova_linha = []
    for j in mapa:
        nova_linha.append(j[i])
    novo_mapa.append(nova_linha)
        
for i in novo_mapa:
    print(i)