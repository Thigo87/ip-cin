def calcular_requisitos(nome, intensidade):
    pass

def possui_ingredientes(moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas):
    pass

def conjurar_feitico(moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas, poder_base, nome, feitico_anterior):
    pass

meta = int(input())
moli = int(input())
lotus = int(input())
cinzas = int(input())
quantidade_tentativas = int(input())

feiticos = []

for i in range(quantidade_tentativas):
    feitico = input()
    feiticos.append(feitico.split())

for i in feiticos:
    i[1] = int(i[1])

print(feiticos)