linhas = int(input())
colunas = int(input())

matriz_valida = True

if linhas == 0 or colunas == 0:
    matriz_valida = False
    print("Dimensões do mapa inválidas!")

if matriz_valida:
    ameacas = []
    print("Avatar: A Lenda de Aang - Planejamento da Invasão!")
    print("Sokka: Mapeando os setores da Nação do Fogo...")
    for i in range(0, linhas):
        linha = []
        for j in range(0, colunas):
            ameaca = int(input())
            linha.append(ameaca)
        ameacas.append(linha)
    
    aliado = input()
    limite_energia = int(input())
    
    for i in range(0, linhas):
        for j in range(0, colunas):
            if i == j:
                ameacas[i][j] *= 2
            if (linhas == colunas) and (i + j == linhas - 1):
                ameacas[i][j] += 5
    
    for i in range(0, linhas):
        for j in range(0, colunas):
            if ameacas[i][j] < 15:
                ameacas[i][j] = 0
            if ameacas[i][j] % 2 != 0:
                ameacas[i][j] += 1
    
    for i in range(0, linhas):
        l = ""
        for j in range(0, colunas):
            if j != colunas - 1:
                l += f"{ameacas[i][j]} "
            else:
                l += f"{ameacas[i][j]}"
        print(l)
        
    soma_total = 0
    for i in range(0, linhas):
        for j in range(0, colunas):
            soma_total += ameacas[i][j]
    
    setor_critico = [0, 0, 0]
    for i in range(0, linhas):
        for j in range(0, colunas):
            if ameacas[i][j] > setor_critico[0]:
                setor_critico[0] = ameacas[i][j]
                setor_critico[1] = i
                setor_critico[2] = j
    
    print("--- RELATÓRIO DO TÚNEL E AMEAÇAS ---")
    print(f"Soma Total de Resistência: {soma_total}")
    print(f"Setor Mais Crítico: ({setor_critico[1]}, {setor_critico[2]}) com valor {setor_critico[0]}")
    
    if soma_total < 100:
        print("Sokka: O mapa revela poucas defesas inimigas!")
        print("Aang: Parece que o caminho está livre.")
        print("Katara: Conseguimos passar sem grandes problemas!")
        print("Estratégia aprovada! O Avatar está pronto para a batalha.")
    elif 100 <= soma_total < 200:
        print("Sokka: Atenção! Detectamos resistência nas defesas da Nação do Fogo.")
        print("Toph: Sinto muitas tropas pelo solo, mas podemos avançar com cuidado.")
        print("Aang: Então vamos atentos. A Equipe Avatar está pronta!")
        print("Estratégia aprovada, mas a invasão será realizada com cautela.")
    elif soma_total >= 200:
        print("Sokka: Alerta! As defesas inimigas são muito fortes!")
        print("Toph: A linha de defesa deles é densa demais para atravessarmos.")
        print("Aang: Então precisamos recuar e repensar nosso plano.")
        print("Alerta vermelho: Nível de ameaça crítico! Invasão adiada.")
    
    sucesso = False
    
    if aliado == "Aang" and (soma_total <= limite_energia):
        sucesso = True
    elif aliado == "Katara":
        pares = 0
        impares = 0
        for i in range(0, linhas):
            for j in range(0, colunas):
                if ameacas[i][j] % 2 == 0:
                    pares += 1
                else:
                    impares += 1
        if pares > impares:
            sucesso = True
    elif aliado == "Toph" and setor_critico[0] <= 50:
        sucesso = True
    elif aliado == "Sokka" and (linhas == colunas):
        sucesso = True
        
    if sucesso:
        print(f"{aliado} usou sua especialidade com maestria e garantiu o sucesso na missão!")
    else:
        print(f"{aliado} encontrou barreiras intransponíveis e a missão precisou ser abortada...")
       