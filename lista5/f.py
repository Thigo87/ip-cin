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

def movimentacao(mapa): #função para movimentação pelo mapa
    pass

mago = {}
guerreiro = {}
bardo = {}
ladino = {}

quantidade_aventureiros = int(input()) #input da quantidade de aventureiros

while quantidade_aventureiros < 1 or quantidade_aventureiros > 4:
    print("Entre 1 e 4") #mensagem de erro
    quantidade_aventureiros = int(input()) #pede o input novamente

for i in range(quantidade_aventureiros): #loop de acordo com a quantidade de aventureiros
    nome, classe = input().split() #recebe o input do nome e da classe do personagem i
    
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