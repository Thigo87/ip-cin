inventario = {}

def adicionar(item, qtd, inventario):
    if not inventario.get(item):
        inventario[item] = qtd
    else:
        inventario[item] += qtd

def remover(item, qtd, inventario):
    if not inventario.get(item) or inventario[item] < qtd:
        print("ERRO! Item não está no Inventário!") if not inventario.get(item) else print("ERRO! Quantidade insuficiente no Inventário!")
    else:
        inventario[item] -= qtd
        if inventario[item] == 0:
            del inventario[item]

acao = ""
while acao != "FIM":
    acao = input()
    if acao != "FIM":
        if acao == "ADICIONAR":
            nome_item = input()
            quantidade_item = int(input())
            adicionar(nome_item, quantidade_item, inventario)
        elif acao == "REMOVER":
            nome_item = input()
            quantidade_item = int(input())
            remover(nome_item, quantidade_item, inventario)

if len(inventario) != 0:
    for item in inventario:
        print(f"{item} - {inventario[item]}")
else:
    print("Inventário Vazio!")