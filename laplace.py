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
            
        
matriz = [[67,0,0],[0,67,0],[0,0,67]]
l = laplace(matriz)
print(l)