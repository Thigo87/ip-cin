def laplace(matriz):
    if len(matriz[0]) == 1:
        return matriz[0]
    elif len(matriz[0]) == 2:
        return (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
    else:
        print("laplace")
        
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(laplace(matriz))