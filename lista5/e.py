INVENTÁRIO = {
    "nível": 0,
    'magias': [],
    'itens': {
        "pás": ["Pá do herói"],
    },
    'troféus': {
        'Capacete do Espectro': 0,
        'Capacete Gélido': 0
    }
}

ITENS = {
    "F": {"secao": "magias", "nome": "Varinha de Chamas", "mensagem": "O que é isso? Sinto um fogo emanando do fundo da minha alma…"},
    "V": {"secao": "magias", "nome": "Varinha de Gelo", "mensagem": "Uma magia nova é sempre bom!"},
    "P": {"secao": "pás", "nome": "Pá Espectral", "mensagem": "Uma pá transparente, que loucura!"},
    "p": {"secao": "pás", "nome": "Pá comum", "mensagem": "Mais uma para minha coleção."},
}

CHEFES = {
    "Specter Knight": {"capacete": "Capacete do Espectro", "nivel_minimo": 2},
    "Polar Knight": {"capacete": "Capacete Gélido", "nivel_minimo": 5},
}

DIRECOES = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

def coleta(item): #coleta de itens no mapa
    if item != "N":
        item_atual = ITENS.get(item, 0)
        secao = ""
        nome = ""
        mensagem = ""
        if item_atual != 0:
            secao = ITENS[item]["secao"]
            nome = ITENS[item]["nome"]
            mensagem = ITENS[item]["mensagem"]

            if secao == "magias":
                INVENTÁRIO[secao].append(nome)
            else:
                INVENTÁRIO["itens"] = {nome : 0} #verificar isso aqui

        return 0, mensagem
        
    else: #aqui aumenta o nível
        return 1, ""


def enfrentar(chefe, inventario, nivel, tem_requisito):
    pass

def relatorio_final(vivo, capacetes, magias, pas):
    if not vivo:
        print("A jornada do herói chega a um triste fim…")
        print("Sua pá não foi capaz de cavar uma saída desse buraco de trevas em que estamos.")
        print("O que restou? Nada… brutal.\n")

    print("======== RELATÓRIO FINAL ========")
    print(f"CAPACETES: {capacetes}")
    print(f"MAGIAS: {magias}")
    print(f"PÁS: {pas}")

def movimentacao(movimento, posicao_atual):
    mov = DIRECOES[movimento]

    x_atualizado = posicao_atual[0] + mov[0]
    y_atualizado = posicao_atual[1] + mov[1]

    if not (0 <= x_atualizado <= 4):
        x_atualizado = posicao_atual[0]

    if not (0 <= y_atualizado <= 4):
        y_atualizado = posicao_atual[1]

    return x_atualizado, y_atualizado
    

print("Shovel Knight, o lendário guerreiro, está de volta! Salvai-nos, ó herói da pá!\n")

magia_adquirida = ""

magias_catalogo = ["Pergaminho dos Elementos", "Varinha da Água", "Grimório de 4 folhas"]

entrada = input()
if entrada == "sim":
    magia = input()
    if magia in magias_catalogo:
        INVENTÁRIO["magias"].append(magia)

#cemitério
print("======== CEMITÉRIO DOS LICHS ========")
print("Um antigo vilarejo tomado pelos mortos. Me pergunto se aquele cavaleiro fantasma se esconde por aqui…")
#black knight
print("Black Knight? O que fazes aqui?")

if len(INVENTÁRIO["magias"]) > 0: #verificando se há algum feitiço que ele adquiriu no mercador
    print("Isso era um desafio?\n")
    mapa_cemiterio = {
    (0, 2): "p",
    (1, 4): "P",
    (2, 1): "N",
    (2, 2): "N",
    (2, 3): "F",
    (3, 3): "N",
    (3, 4): "N",
    (4, 0): "p",
    (4, 1): "X",
    }  

    posicao_atual = [[0, 0], "simbolo"]

    while posicao_atual[1] != "X":
        direcao = input()
        posicao_atual[0] = movimentacao(direcao, posicao_atual[0])
        posicao_atual[1] = mapa_cemiterio.get((posicao_atual[0][0], posicao_atual[0][1]), "0")
        coleta(posicao_atual[1])

    print(INVENTÁRIO)

    

else: #caso não exista feitiço ele morre
    relatorio_final(False, "NENHUM", "NENHUM", INVENTÁRIO["itens"]["pás"][0])