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
    
