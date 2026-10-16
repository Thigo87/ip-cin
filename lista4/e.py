def bencaos(bencaos_obtidas):
    bencaos = 0
    deuses = ["AFRODITE", "ARES", "ARTEMIS", "ATENA", "DEMETER", "DIONISIO", "HERMES", "POSEIDON", "ZEUS"]
    deusGrego = ""
    while deusGrego != "PARAR":
        deusGrego = input()
        
        if deusGrego != "PARAR": 
            combinada = False        
            if deusGrego == "COMBINADA":
                combinada = True
            
            if combinada:
                combinada_1 = input()
                combinada_2 = input()
                if combinada_1 not in deuses or combinada_2 not in deuses:
                    print("Zagreu: Uma Bênção Combinada assim? Acho que você está brincando comigo.")
                elif (combinada_1 or combinada_2) not in bencaos_obtidas:
                    print("Zagreu: Eu ainda não tenho nenhuma Bênção desse(a) Deus(a), não posso combiná-la")
                elif combinada_1 == combinada_2:
                    print("Zagreu: Os dois Deuses precisam diferentes para realizar uma Bênção Combinada...")
                elif (combinada_1 or combinada_2) == "HERMES":
                    print("Zagreu: Uma Bênção Combinada com Hermes? Acho que ele é competitivo demais pra cooperar com os outros.")
                else:
                    print(f"Zagreu foi abençoado por uma Bênção Combinada de {combinada_1} e {combinada_2}.")
                    bencaos += 1
                    bencaos_obtidas.append(deusGrego)
            else:
                bencaos += 1
                if deusGrego in deuses:
                    bencaos_obtidas.append(deusGrego)
                    print(f"Zagreu obteve uma Bênção de {deusGrego}.")
                else:
                    print(f"Zagreu: Ah, claro. A Bênção de {deusGrego}. Como pude esquecer? Tenho certeza de que meu pai também deve ter esquecido de mencioná-lo(a)... Você está brincando comigo não é?.")
        else:
            print("")
    return bencaos

def multiplicacaoMatrix(matrizA, matrizB):
    linhasA  = len(matrizA)
    colunasA = len(matrizA[0])
    colunasB = len(matrizB[0])
    
    matriz_final = []
    for i in range(linhasA):
        linha = []
        for j in range(colunasB):
            soma = 0
            for k in range(colunasA):
                soma += matrizA[i][k] * matrizB[k][j] 
            linha.append(soma)
        matriz_final.append(linha)
    
    return matriz_final
    
def tartaro(lista_nomes, lista_bencaos):
    qntd_nomes = len(lista_nomes)
    for n in range(qntd_nomes - 1):
        for m in range(qntd_nomes - n - 1):
            if lista_nomes[m] > lista_nomes[m + 1]:
                lista_nomes[m], lista_nomes[m + 1] = lista_nomes[m + 1], lista_nomes[m]
    lista_em_ordem_alfabetica = ""
    for nome in lista_nomes:
        lista_em_ordem_alfabetica += f"{nome}, "
        
    print(f"Zagreu: Aqui está sua papelada: {lista_em_ordem_alfabetica[:(len(lista_em_ordem_alfabetica) - 2)]}\n")
        
    vivo = True
    
    bencaos(lista_bencaos)
    
    if len(lista_bencaos) < 3:
        vivo = False 
    
    return vivo

def asfodelo(matrizA, matrizB, lista_bencaos):
    resultado = multiplicacaoMatrix(matrizA, matrizB)
    maiorValor = [0, 0, 0]
    for i in range(len(resultado)):
        for j in range(len(resultado[0])):
            if resultado[i][j] > maiorValor[0]:
                maiorValor[0] = resultado[i][j]
                maiorValor[1] = i
                maiorValor[2] = j
    vivo = True
    
    print(f"Zagreu: devo lançar minha vara de pesca nesse ponto: ({maiorValor[1]}, {maiorValor[2]})\n")
    
    bencaos(lista_bencaos)
    
    if len(lista_bencaos) < 6:
        vivo = False
    return vivo

def elisio(lista_bencaos):
    legado = 0
    while legado < 200:
        pontuacao = 0
        heroi = input()
        nome, titulo = heroi.split(" O ")
        
        if nome == "Hércules":
            pontuacao += 50
        elif nome == "Aquiles":
            pontuacao += 40
        elif nome == "Odisseu":
            pontuacao += 35
        else:
            pontuacao += 20
        
        if titulo == "Imortal":
            pontuacao *= 1.5
        elif titulo == "Forte":
            pontuacao *= 1.2
        elif titulo == "Grande":
            pontuacao += 15
        else:
            pontuacao += 10
        
        print(f"O Herói: {nome} O {titulo} adicionou {pontuacao} pontos de Legado.")
        legado += pontuacao
        
    print("Zagreu: Acho que já fizemos história o suficiente por hoje.\n")
            
    vivo = True
    
    bencaos(lista_bencaos)
     
    if len(lista_bencaos) < 9:
        vivo = False       
    return vivo
    
def temploDeEstige():
    print("O Templo de Estige... o último obstáculo entre você e a superfície.\n")
    vidaZagreu = 100
    vidaHades = 200
    
    esquiva = False
    especialHades = False
    segundaFase = False
    danoHades = 0
    ataquesHades = 0
    
    while vidaZagreu > 0 and vidaHades > 0:
        acao = input()
        esquiva = False
        if acao == "ATACAR":
            print("Zagreu golpeia Hades, causando 20 de dano.")
            vidaHades -= 20
        elif acao == "ATAQUE ESPECIAL":
            print("Zagreu golpeia Hades com um ataque especial, causando 40 de dano.")
            vidaHades -= 40
        elif acao == "ESQUIVA":
            print("Zagreu esquiva do ataque de Hades, evitando o dano.")
            esquiva = True
        
        if vidaHades > 0:
            ataquesHades += 1
            if ataquesHades == 3:
                if not esquiva:
                    especialHades = True
                    ataquesHades = 0
                    print("Hades: Desapareça!")
                else:
                    ataquesHades = 0
            
            if vidaHades <= 100:
                if not segundaFase:
                    print("")
                    print("Hades: Chega! Isso acaba agora!")
                    print("")
                    segundaFase = True
                if especialHades:
                    danoHades = 100
                    especialHades = False
                else:
                    danoHades = 25
                
            else:
                if not esquiva:
                    if especialHades:
                        danoHades = 50
                        especialHades = False
                    else:
                        danoHades = 15
                
            if not esquiva:
                vidaZagreu -= danoHades
                print(f"Hades causou {danoHades} de dano em Zagreu.")

        if ataquesHades == 2 and vidaZagreu > 0:
            print("Zagreu: Meu pai parece estar carregando um forte ataque, é melhor desviar!")
    print("")
    
    if vidaZagreu > 0:
        print("O senhor do Submundo cai diante de Zagreu. Pela primeira vez, não há nada entre ele e a superfície.")
        print("O portão se abre diante de você.")
        print("Zagreu finalmente deixa o Submundo para trás e sente o calor do sol tocar seu rosto. Pela primeira vez, a superfície está diante de seus olhos.")
        print("Você conseguiu escapar. A tentativa foi concluída.")
    else:
        print("Zagreu: Me desculpe, mãe. Foi tão perto...")

print("O portão se abre diante de você, revelando o caminho para o Submundo. Uma nova tentativa começa agora.\n")
lista_bencaos = []

vivo = True 
lista_nomes = input()
vivo = tartaro(lista_nomes.split(", "), lista_bencaos)
if vivo:
    matrizA = []
    matrizB = []
    #recebendo os inputs para a matriz A
    for i in range(3):
        linha = input()
        matrizA.append(linha.split())
    
    #recebendo os inputs da matriz B
    for i in range(3):
        linha = input()
        matrizB.append(linha.split())
    
    #transformando os itens de A em inteiros
    for i in range(len(matrizA)):
        for j in range(len(matrizA[0])):
            matrizA[i][j] = int(matrizA[i][j])

    #transformando os itens de B em inteiros
    for i in range(len(matrizB)):
        for j in range(len(matrizB[0])):
            matrizB[i][j] = int(matrizB[i][j])

    vivo = asfodelo(matrizA, matrizB, lista_bencaos)
    if vivo:
        vivo = elisio(lista_bencaos)
        
        if vivo:
            temploDeEstige()
        else:
            print("Zagreu cai, derrotado mais uma vez. Seu corpo se desfaz, retornando ao lugar que conhece tão bem.")
    else:
        print("Zagreu cai, derrotado mais uma vez. Seu corpo se desfaz, retornando ao lugar que conhece tão bem.")
else:
    print("Zagreu cai, derrotado mais uma vez. Seu corpo se desfaz, retornando ao lugar que conhece tão bem.")