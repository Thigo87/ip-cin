print("--- FASE 1: A VARREDURA ---")

matriz_principal = []

n = int(input())
for i in range(0, n):
    itens = input()
    matriz_principal.append(itens.split(", "))

limites_sub_matriz = input()

limites_sub_matriz = limites_sub_matriz.split()

linha_inicio = int(limites_sub_matriz[0])
linha_fim = int(limites_sub_matriz[1])
coluna_inicio = int(limites_sub_matriz[2])
coluna_fim = int(limites_sub_matriz[3])

print("Lisbon: Jane, focamos as buscas no quadrante delimitado.")

for i in range(linha_inicio, linha_fim):
    linha = ""
    for j in range(coluna_inicio, coluna_fim):
        if j != coluna_fim - 1:
            linha += f"'{matriz_principal[i][j]}', "
        else:
            linha += f"'{matriz_principal[i][j]}'"
    print(f"[{linha}]")

sangue = 0
arma = 0
smiley = ["Nao", 0]

for i in range(linha_inicio, linha_fim):
    for j in range(coluna_inicio, coluna_fim):
        if matriz_principal[i][j] == "Sangue":
            sangue += 1
        elif matriz_principal[i][j] == "Arma":
            arma += 1
        elif matriz_principal[i][j] == "Smiley":
            smiley[0] = "Sim"
            smiley[1] += 1

print(f"Evidencias encontradas: Sangue ({sangue}), Arma ({arma}). Smiley ({smiley[0]})")
print("")
print("--- FASE 2: A MATRIZ DE EVIDÊNCIAS ---")

n_m_evidencias = input()
n_m_evidencias = n_m_evidencias.split()

numero_linhas_matriz_evidencias = int(n_m_evidencias[0])
numero_colunas_matriz_evidencias = int(n_m_evidencias[1])

matriz_evidencias = []

for i in range(0, numero_linhas_matriz_evidencias):
    numeros = input()
    linha = numeros.split(" ")
    for a in range(0, len(linha)):
        linha[a] = int(linha[a])
    matriz_evidencias.append(linha)


limiar_evidencia = int(input())

print("Patrick Jane: Às vezes, a verdade está escondida bem diante dos nossos olhos.")

matriz_binaria = []

for i in range(0, numero_linhas_matriz_evidencias):
    linha = []
    for j in range(0, numero_colunas_matriz_evidencias):
        if matriz_evidencias[i][j] >= limiar_evidencia:
            linha.append(1)
        else:
            linha.append(0)
    matriz_binaria.append(linha)

for i in range(0, numero_linhas_matriz_evidencias):
    linha = ""
    for j in range(0, numero_colunas_matriz_evidencias):
        if j != numero_colunas_matriz_evidencias - 1:
            linha += f"{matriz_binaria[i][j]} "
        else:
            linha += f"{matriz_binaria[i][j]}"
    print(linha)

assinatura = ["11011", "10001", "01110"]
linha_inicial_assinatura = 0
coluna_inicial_assinatura = 0
existe_assinatura = False

for i in range(0, numero_linhas_matriz_evidencias):
    linha = ""
    for j in range(0, numero_colunas_matriz_evidencias):
        linha += str(matriz_binaria[i][j])
    if assinatura[0] in linha:
        linha_inicial_assinatura = i
        indice = len(linha)
        inicio = False
        for k in range(0, indice):
            if inicio == False:
                if assinatura[0] not in linha[k::]:
                    coluna_inicial_assinatura = k - 1
                    inicio = True
        linha_2 = ""
        linha_3 = ""
        for j in range(0, numero_colunas_matriz_evidencias):
            linha_2 += str(matriz_binaria[i + 1][j])
        
        for j in range(0, numero_colunas_matriz_evidencias):
            linha_3 += str(matriz_binaria[i + 2][j])
        
        meio = False
        fim = False
        if assinatura[1] in linha_2[coluna_inicial_assinatura::]:
            meio = True
        
        if assinatura[2] in linha_3[coluna_inicial_assinatura::]:
            fim = True
        
        if inicio and meio and fim:
            existe_assinatura = True
            
red_john = False

if existe_assinatura or smiley[0] == "Sim":
    red_john = True

if existe_assinatura:
    print("Patrick Jane: Eu conheço esse sorriso.")
    print("RED JOHN DEIXOU UMA ASSINATURA!")
    print(f"ASSINATURA ENCONTRADA EM [{linha_inicial_assinatura}][{coluna_inicial_assinatura}]")
else:
    print("Patrick Jane: Nada aqui parece familiar.")

if red_john:
    print("")
    print("--- FASE 3: A MENSAGEM ---")
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    
    mensagem_codificada = input()
    mensagem = ""
    
    mensagem_codificada = [int(char) for char in mensagem_codificada.split()]
    mensagem_codificada = [alfabeto[(x // 2) % 27] if x % 2 == 0 else alfabeto[(x * 3 + 1) % 27] for x in mensagem_codificada]
    
    mensagem = "".join(mensagem_codificada)
        
    print(f'Mensagem decodificada: "{mensagem}"')
    print("Jane: Ele acha que é mais esperto que eu. Nós vamos pegá-lo.")
    
else:
    print("")
    print("--- FASE 3: O CÓDIGO ---")
    nota_cifrada = input()
    nota_cifrada = nota_cifrada[::-1]
    
    mensagem = ""
    
    for i in range(0, len(nota_cifrada)):
        if i % 2 == 0:
            mensagem += nota_cifrada[i]
    
    mensagem_decodificada = ""
    
    for i in mensagem:
        if i.islower():
            mensagem_decodificada += i.upper()
        else:
            mensagem_decodificada += i.lower()
    
    grau_obsessao = 0
    
    for i in mensagem:
        if i == "J" or i == "j":
            grau_obsessao += 1
            
    print("Patrick Jane: Vamos ver o que ele quis dizer dessa vez.")
    print("MENSAGEM DECODIFICADA!")
    print(f"Patrick Jane: '{mensagem_decodificada}'...")
    print("Patrick Jane: Esse caso acabou de dar uma reviravolta interessante.")
    print(f"Grau de Obsessão: {grau_obsessao} aparição(ões) da letra J na mensagem.")
    print("--- CASO ENCERRADO (por enquanto...) ---")