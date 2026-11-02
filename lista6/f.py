def laplace(matriz):
    if len(matriz[0]) == 1:
        return matriz[0][0]
    elif len(matriz[0]) == 2:
        return (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
    else:
        primeira_linha = matriz[0]
        tamanho = len(primeira_linha)
        determinante = 0
        for i in range(tamanho):
            nova_matriz = []
            for j in range(tamanho):
                if j != 0:
                    nova_linha = []
                    for k in range(tamanho):
                        if k != i:
                            nova_linha.append(matriz[j][k])
                    nova_matriz.append(nova_linha)
            if i % 2 == 0:
                determinante += primeira_linha[i] * laplace(nova_matriz)
            else:
                determinante += (-1) * primeira_linha[i] * laplace(nova_matriz)
        
        return determinante
    
qtd_linhas = 1
qtd_colunas = 2
matriz_base = []
matriz_enfeites = []

print("🎄 O Natal chegou na Cozinha! Vamos preparar um Biscoito digno do Papai Noel!")
while qtd_colunas != qtd_linhas or qtd_colunas <= 0 or qtd_linhas <= 0:
    qtd_linhas, qtd_colunas = input().split()
    qtd_linhas = int(qtd_linhas)
    qtd_colunas = int(qtd_colunas)
    
    if qtd_linhas != qtd_colunas or (qtd_colunas <= 0 or qtd_linhas <= 0):
        print("Esse Biscoito não cabe na Receita! Precisamos de um Quadrado com dimensões positivas!")

print("🍪 Hora de preparar a Massa! Qual a Gostosura de cada pedaço?")
        
for linha in range(qtd_linhas):
    nova_linha = input().split()
    for i in range(len(nova_linha)):
        nova_linha[i] = int(nova_linha[i])
    matriz_base.append(nova_linha)

print("Vamos dar um toque de Magia! Onde colocaremos os Enfeites Natalinos?")

for linha in range(qtd_linhas):
    nova_linha = input().split()
    matriz_enfeites.append(nova_linha)

enfeites_adicionados = []

for i in range(len(matriz_enfeites)):
    for j in range(len(matriz_enfeites)):
        elemento = matriz_enfeites[i][j]
        if elemento == "E":
            matriz_base[i][j] = matriz_base[i][j] * 2
            enfeites_adicionados.append("E")
        elif elemento == "F":
            matriz_base[i][j] = matriz_base[i][j] * -1
            enfeites_adicionados.append("F")
        elif elemento == "P":
            matriz_base[i][j] = matriz_base[i][j] + 5
            enfeites_adicionados.append("P")
        elif elemento == "A":
            matriz_base[i][j] = matriz_base[i][j] ** 2
            enfeites_adicionados.append("A")

enfeites = len(enfeites_adicionados)
gostosura = laplace(matriz_base)

print("Vamos a Análise Final!")
print(f"\nGostosura: {gostosura}")

if gostosura < 0:
    print("Nem o Grinch teria Coragem de provar esse Biscoito!")
elif gostosura == 0:
    if enfeites == 0:
        print("A Magia do Biscoito se Anulou.")
    else:
        print("Tanta Decoração para nada! A Magia do Biscoito se Anulou.")
else:
    qtd_flocos = 0
    qtd_estrelas = 0
    qtd_presentes = 0
    qtd_arvores = 0
    
    for item in enfeites_adicionados:
        if item == "F":
            qtd_flocos += 1
        elif item == "E":
            qtd_estrelas += 1
        elif item == "P":
            qtd_presentes += 1
        elif item == "A":
            qtd_arvores += 1
            
    if qtd_arvores >= 1 and qtd_presentes >= 1 and qtd_flocos >= 1 and qtd_estrelas >= 1:
        print("Um Pedaço de cada Encanto Natalino! Esse vai para o Papai Noel! 🎅")
    elif qtd_flocos > (qtd_estrelas + qtd_presentes + qtd_arvores):
        print("Gostoso e Congelante! Sirva com uma Caneca de Chocolate Quente! ❄️")
    elif qtd_arvores >= 1 and qtd_flocos == 0:
        print("Uma Floresta de gostosura! As Renas vão Adorar! 🎄")
    else:
        print("Receita Aprovada! Já pode colocar ao lado do Copo de Leite! 🥛")