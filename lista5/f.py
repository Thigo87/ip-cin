def decrypt(frase, chave): #função para descriptografar o item
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    nova_frase = ""
    for letra in frase: #verifico cada letra da frase
        if letra == " ":
            nova_frase += " "
        else:
            nova_frase += alfabeto[alfabeto.index(letra) - chave]
    return nova_frase 

def montagem_inventario(string): #função para montar o inventário
    catalogo = {"arma" : ['cajado', 'machado grande', 'adaga', 'adaga dupla'], 
                "utilidade" : ['grimorio', 'escudo de madeira', 'alaude', 'ferramentas de ladrao'], 
                "consumivel" : ['pergaminho oculto', 'racao de viagem', 'pocao de cura', 'bomba de fumaca']}
    
    string_criptografada, chave_da_cifra, poder_do_item = string.split(" - ") #recebendo cada informação que está separara por -
    item = decrypt(string_criptografada, int(chave_da_cifra)) #descriptografando o item
    inventario = {} #criando o inventário vazio
    
    for tipo in catalogo: #verificando em qual tipo o item se encaixa para adicionar ao inventário
        if item in catalogo[tipo]:
            inventario.update({item : {"tipo" : tipo, "poder" : poder_do_item}})
    
    return inventario

def ePrimo(num): #função para verificar se o número é primo
    divisores = 0

    for n in range(1, num + 1): #verifico quais são os divisores do número num
        if num // n == num / n:
            divisores += 1

    if divisores > 2 or num == 0: #se ele tiver mais que dois divisores (ele mesmo e 1) ou for 0, não é primo
        return False
    else: #caso contrário é primo
        return True

def quadradoPerfeito(num):
    if int(num ** 0.5) == float(num ** 0.5) and num != 0:
        return True
    else:
        return False

def movimentacao(mapa, posicao_atual): #função para movimentação pelo mapa
    maior_valor = 0
    proxima_posicao = [0, 0]
    x, y = posicao_atual[0], posicao_atual[1] #separando as coordenadas

    limites = len(mapa[0]) #definindo os limites do mapa

    #verificando ao redor qual o maior valor
    if 1 <= x:
        if mapa[x - 1][y] > maior_valor:
            maior_valor = mapa[x - 1][y]
            proxima_posicao = [x - 1, y]
    if limites - 1 > x:
        if mapa[x + 1][y] > maior_valor:
                    maior_valor = mapa[x + 1][y]
                    proxima_posicao = [x + 1, y]

    if 1 <= y:
            if mapa[x][y - 1] > maior_valor:
                maior_valor = mapa[x][y - 1]
                proxima_posicao = [x, y - 1]
    if limites - 1 > y:
        if mapa[x][y + 1] > maior_valor:
                    maior_valor = mapa[x][y + 1]
                    proxima_posicao = [x, y + 1]
    

    return proxima_posicao, maior_valor

mago = {}
guerreiro = {}
bardo = {}
ladino = {}
personagens = []

quantidade_aventureiros = int(input()) #input da quantidade de aventureiros

while quantidade_aventureiros < 1 or quantidade_aventureiros > 4:
    print("Entre 1 e 4") #mensagem de erro
    quantidade_aventureiros = int(input()) #pede o input novamente

for i in range(quantidade_aventureiros): #loop de acordo com a quantidade de aventureiros
    nome, classe = input().split() #recebe o input do nome e da classe do personagem i
    personagens.append(nome)
    
    #verificando os inputs e separando de acordo com a classe
    if classe == "B":
        bardo.update({"nome" : nome, "inventario":{}})
        frase = ""
        while frase != "pronto":
            frase = input()
            if frase != "pronto":
                bardo["inventario"].update(montagem_inventario(frase))
                
    elif classe == "G":
        guerreiro.update({"nome" : nome, "inventario":{}})
        frase = ""
        while frase != "pronto":
            frase = input()
            if frase != "pronto":
                guerreiro["inventario"].update(montagem_inventario(frase))
                
    elif classe == "L":
        ladino.update({"nome" : nome, "inventario":{}})
        frase = ""
        while frase != "pronto":
            frase = input()
            if frase != "pronto":
                ladino["inventario"].update(montagem_inventario(frase))

    elif classe == "M":
        mago.update({"nome" : nome, "inventario":{}})
        frase = ""
        while frase != "pronto":
            frase = input()
            if frase != "pronto":
                mago["inventario"].update(montagem_inventario(frase))

#remover até o ==========
print(mago)
print(guerreiro)
print(bardo)
print(ladino)
#==========================

#criando o mapa
mapa = []
qt_linhas_colunas = int(input())

for linha in range(qt_linhas_colunas):
    linha = []
    linha_da_matriz = input()
    for item in linha_da_matriz.split():
        linha.append(int(item))
    mapa.append(linha)

print(mapa)

#configurando a posição inicial e o valor dessa posição
posicao_atual = [0, 0]
valor_posicao = 0

#loop da movimentação
while valor_posicao != 99:
    posicao_atual, valor_posicao = movimentacao(mapa, posicao_atual)
    if ePrimo(valor_posicao): #caiu na armadilha
        tipo_armadilha = input()

        if tipo_armadilha == "flechas": #continuar aqui
            if "escudo de madeira" in guerreiro["inventario"]:
                del guerreiro["inventario"]["escudo de madeira"]
            
        elif tipo_armadilha == "beholder":
            pass

    if quadradoPerfeito(valor_posicao): #sala de looting
        pass