def calcular_requisitos(nome, intensidade):
    custo_moli = 0
    custo_lotus = 0
    custo_cinzas = 0
    poder_base = 0
    
    if nome == "LUA":
        custo_moli = intensidade
        custo_lotus = 1
        poder_base = 10*intensidade
    elif nome == "SOMBRAS":
        custo_lotus = intensidade
        custo_cinzas = 2
        poder_base = 12*intensidade
    elif nome == "FAMILIAR":
        custo_moli = 1
        custo_lotus = 1
        custo_cinzas = intensidade
        poder_base = 15*intensidade
    
    return  custo_moli, custo_lotus, custo_cinzas, poder_base

def possui_ingredientes(moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas):
    suficiente = False
    
    if moli >= custo_moli and lotus >= custo_lotus and cinzas >= custo_cinzas:
        suficiente = True
    
    return suficiente

def conjurar_feitico(moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas, poder_base, nome, feitico_anterior):
    nova_qntd_moli = moli - custo_moli
    nova_qntd_lotus = lotus - custo_lotus
    nova_qntd_cinzas = cinzas - custo_cinzas
    poder_obtido = poder_base
    
    if nome != feitico_anterior:
        bonus_recebido = 5
    else:
        bonus_recebido = 0
    
    return nova_qntd_moli, nova_qntd_lotus, nova_qntd_cinzas, poder_obtido, bonus_recebido
    

meta = int(input())
moli = int(input())
lotus = int(input())
cinzas = int(input())
quantidade_tentativas = int(input())

feiticos = []

poder_total = 0

for i in range(quantidade_tentativas):
    feitico = input()
    feiticos.append(feitico.split())

counter = 0

for i in range(len(feiticos)):
    nome = feiticos[i][0]
    feiticos[i][1] = int(feiticos[i][1])
    feitico_anterior = feiticos[i-1][0] if i > 0 else feiticos[i][0]
    custo_moli, custo_lotus, custo_cinzas, poder_base = calcular_requisitos(feiticos[i][0], feiticos[i][1])
    
    suficiente =  possui_ingredientes(moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas)
    
    if suficiente:
        counter += 1
        moli, lotus, cinzas, poder, bonus = conjurar_feitico(moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas, poder_base, nome, feitico_anterior)
        poder_obtido = poder + bonus
        poder_total += poder_obtido
        print(f"Melinoë conjurou {nome} e obteve {poder_obtido} de poder.")
        if bonus != 0:
            print("Sinergia lunar ativada! Selene concedeu 5 de poder extra.\nHécate: A luz de Selene responde à sua feitiçaria. Faça-a valer.")
        else:
            if counter == 1:
                print("Hécate: Foi para isto que treinamos todas essas noites, Melinoë.")
            else:
                print("Hécate: Disciplina, Melinoë. Uma bruxa vence antes mesmo de deixar a Encruzilhada.")
        print("Que assim seja!")
    
    else:
        print(f"Ingredientes insuficientes para conjurar {nome}.\nHécate: Intenção sem preparo não basta. Reúna os ingredientes e tente outra vez.")

print("")
print(f"Poder acumulado: {poder_total}\nIngredientes restantes: {moli} moli, {lotus} lotus e {cinzas} cinzas.")

if poder_total >= meta:
    print("Melinoë está pronta para enfrentar Cronos.\nHécate: Você está pronta para partir. Lembre-se do que aprendeu na Encruzilhada — e retorne para nós.")
else:
    print("Melinoë precisa se preparar melhor antes de enfrentar Cronos.\nHécate: Cronos não terá piedade de você. Eu tampouco terei durante seu treinamento.")