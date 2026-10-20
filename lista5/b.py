inventario = {"Vax":{}, "Pike":{}, "Grog":{}, "Percy":{}, "Scanlan": {}, "Vex": {}, "Keyleth": {}}
   

entrada = ""
while entrada.upper() != "FIM":
    entrada = input()
    if entrada.upper() != "FIM":
        entrada_dividida = entrada.split(" , ")
        nome_heroi = entrada_dividida[0]
        item = entrada_dividida[1]
        poder = int(entrada_dividida[2])

        if nome_heroi == "Vex" and item == "Fenthras":
            print("Um arco mágico, capaz de controlar todos os elementos? isso é perfeito para mim querido!")
        elif nome_heroi == "Grog" and item == "Manoplas de Titanstone":
            print("Estou maior agora, e pronto para entrar em fúria!")
        elif nome_heroi == "Vax" and item == "Adaga Mágica":
            print("Uma arma dada pela própria rainha dos corvos, agora apenas preciso saber se isso é uma dádiva ou uma maldição.")
        elif nome_heroi == "Scanlan" and item == "Caça Mitos":
            print("A espada lendária capaz de matar todos os Dragões... nas mãos do Scanlan?!")
        elif nome_heroi == "Keyleth" and item == "Pináculo da Confluência":
            print("Com isso e meu aramenté completo, a natureza inteira estará sobre meu controle.")
        elif nome_heroi == "Percy" and item == "The List":
            print("Não, ele novamente não, Orthax já me dominou uma vez, não posso deixar isso acontecer de novo.")
        elif nome_heroi == "Pike" and item == "Placa do Mártir":
            print("Everlight, espero que um dia você me perdoe, mas não vou mais depender de você.")
        
        inventario[nome_heroi].update({item:poder}) 

for personagem in inventario:
    if len(inventario[personagem]) == 0:
        print(f"{personagem} não possui nenhuma arma.")
    else:
        mais_forte = ""
        poder = 0
        for item in inventario[personagem]:
            pontos = int(inventario[personagem][item])
            if pontos > poder:
                mais_forte = item
                poder = pontos
        print(f"A arma mais forte de {personagem} é a {mais_forte} com {poder} Pontos de Poder.")
