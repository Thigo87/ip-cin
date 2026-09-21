cadastro_heroi = ""
herois = []
ameacas = []

print("========================================")
print("GDA - HERO DISPATCH SYSTEM")
print("========================================")
print("[ROBOT] Sistema de despacho iniciado.")

while cadastro_heroi.upper() != "FIM":
    cadastro_heroi = input()
    if cadastro_heroi.upper() != "FIM":
        herois.append(cadastro_heroi.split(" - "))

print(f"[ROBOT] {len(herois)} heróis disponíveis.")

n = int(input())
for i in range(0, n):
    ameaca = input()
    ameacas.append(ameaca.split("-"))

for i in herois:
    indice = 0
    for j in range(0, len(i)):
        i[j] = i[j].strip()
        if i[j].isnumeric():
            i[j] = int(i[j])

for i in ameacas:
    indice = 0
    for j in range(0, len(i)):
        i[j] = i[j].strip()
        if i[j].isnumeric():
            i[j] = int(i[j])  

compatibilidade = []

for i in ameacas:
    compatibilidade = []
    for m in herois:
        pontuacao = m[1] + m[2] + m[3] + m[4] + m[5]
        compatibilidade.append([m[0], pontuacao])
    print("========================================")
    print("NOVA AMEAÇA DETECTADA")
    print("========================================")
    print(f"AMEAÇA: {i[0]}")
    print(f"NÍVEL DE DIFICULDADE: {i[1]}")
    print(f"PRIORIDADE: {i[2]}")
    print("[ROBOT] Analisando heróis disponíveis...")
    print("[ROBOT] Calculando compatibilidade...")
    print("[ROBOT] Análise concluída.")
    print("========================================")
    print("RANKING DE HERÓIS")
    print("========================================")
    if i[2] == "Força":
        for j in range(0, len(compatibilidade)):
            compatibilidade[j][1] += herois[j][1]     
    elif i[2] == "Resistência":
        for j in range(0, len(compatibilidade)):
            compatibilidade[j][1] += herois[j][2]
    elif i[2] == "Velocidade":
        for j in range(0, len(compatibilidade)):
            compatibilidade[j][1] += herois[j][3]
    elif i[2] == "Inteligência":
        for j in range(0, len(compatibilidade)):
            compatibilidade[j][1] += herois[j][4]
    elif i[2] == "Experiência":
        for j in range(0, len(compatibilidade)):
            compatibilidade[j][1] += herois[j][5]

    ranking = compatibilidade
    for j in range(0, len(ranking) - 1):
        for k in range(len(ranking) - j - 1):
            if ranking[k][1] < ranking[k + 1][1]:
                ranking[k],ranking[k + 1] = ranking[k + 1], ranking[k]
            elif ranking[k][1] == ranking[k + 1][1]:
                if i[2] == "Força":
                    if herois[k][1] < herois[k + 1][1]:
                        ranking[k],ranking[k + 1] = ranking[k + 1], ranking[k]
                elif i[2] == "Resistência":
                     if herois[k][2] < herois[k + 1][2]:
                        ranking[k],ranking[k + 1] = ranking[k + 1], ranking[k]
                elif i[2] == "Velocidade":
                     if herois[k][3] < herois[k + 1][3]:
                        ranking[k],ranking[k + 1] = ranking[k + 1], ranking[k]
                elif i[2] == "Inteligência":
                     if herois[k][4] < herois[k + 1][4]:
                        ranking[k],ranking[k + 1] = ranking[k + 1], ranking[k]
                elif i[2] == "Experiência":
                    if herois[k][5] < herois[k + 1][5]:
                        ranking[k],ranking[k + 1] = ranking[k + 1], ranking[k]
                        
    for j in range(0, len(ranking)):        
        print(f"{j + 1}. {ranking[j][0]} - {ranking[j][1]} pontos")
    
    print("----------------------------------------")
    classificacao = ""
    qntd = 0
    if 1 <= i[1] <= 30:
        classificacao = "SIMPLES"
        qntd = 1
    elif 31 <= i[1] <= 70:
        classificacao = "MODERADA"
        qntd = 2
    elif 71 <= i[1] <= 100:
        classificacao = "CRÍTICA"
        qntd = 3
        
    print(f"[ROBOT] Ameaça {classificacao}.")
    print(f"[ROBOT] {qntd} herói(s) serão despachados.")
    
    if qntd > len(herois):
        print("[ROBOT] ALERTA!")
        print(f"[ROBOT] São necessários {qntd} heróis,")
        print(f"[ROBOT] mas apenas {len(herois)} estão disponíveis.")
        print("[ROBOT] Despachando todos os heróis disponíveis.")
        print("EQUIPE DESPACHADA:")
        for k in ranking:
            print(f"> {i}")
    else:
        print("[CECIL] Equipe selecionada para a missão.")
        print("EQUIPE DESPACHADA:")
        for k in range(0, qntd):
            print(f"> {ranking[k][0]}")
    print("========================================")