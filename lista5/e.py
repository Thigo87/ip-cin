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
                INVENTÁRIO["itens"][secao].append(nome) #verificar isso aqui

        return 0, mensagem
        
    else: #aqui aumenta o nível
        return 1, ""


def enfrentar(chefe, inventario, nivel, tem_requisito):
    if tem_requisito and nivel >= CHEFES[chefe]["nivel_minimo"]:
        inventario["troféus"][CHEFES[chefe]["capacete"]] += 1
        return True
    else:
        return False

def relatorio_final(vivo, capacetes, magias, pas):
    if not vivo:
        print("A jornada do herói chega a um triste fim…")
        print("Sua pá não foi capaz de cavar uma saída desse buraco de trevas em que estamos.")
        print("O que restou? Nada… brutal.\n")

    capacetes_adquiridos = ""
    
    for capacete in capacetes:
        if capacetes[capacete] == 1:
            capacetes_adquiridos += f"{capacete}, "
    
    if capacetes_adquiridos == "":
        capacetes_adquiridos = "NENHUM"
    else:    
        capacetes_adquiridos = capacetes_adquiridos[:(len(capacetes_adquiridos) - 2)]
        
    magias_adquiridas = ""
    
    for magia in magias:
        magias_adquiridas += f"{magia}, "
        
    if magias_adquiridas == "":
        magias_adquiridas = "NENHUM"
    else:    
        magias_adquiridas = magias_adquiridas[:(len(magias_adquiridas) - 2)]
    
    pas_adquiridas = ""
        
    for pa in pas:
        pas_adquiridas += f"{pa}, "
          
    pas_adquiridas = pas_adquiridas[:(len(pas_adquiridas) - 2)]
    
    print("======== RELATÓRIO FINAL ========")
    print(f"CAPACETES: {capacetes_adquiridos}")
    print(f"MAGIAS: {magias_adquiridas}")
    print(f"PÁS: {pas_adquiridas}")

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
        xp, mensagem = coleta(posicao_atual[1])
        INVENTÁRIO["nível"] += xp
        if mensagem != "":
            print(mensagem)
        
    tem_requisitos = False
    if "Pá Espectral" in INVENTÁRIO["itens"]["pás"]:
         tem_requisitos = True
    
    print("Está na hora de caçar fantasmas!")
    batalha = enfrentar("Specter Knight", INVENTÁRIO, INVENTÁRIO["nível"], tem_requisitos)
    if batalha == True: #venceu a batalha
        print("")
        
        #nova fase
        print("======== NAVIO ENCALHADO ========")
        print("Uma embarcação antiga do Rei liderada pelo meu antigo mentor, o que será que encontrarei?")
        #encontrou o black knight
        print("Você de novo? E que neve toda é essa?")
        
        #verificando se ele tem 3 pás
        if len(INVENTÁRIO["itens"]["pás"]) >= 3:
            print("Engraçado tentar parar um mestre das pás com neve, você se superou dessa vez!")
        
        else: #se não tiver
            print("Que saco! Onde estão minhas outras pás?")
            INVENTÁRIO["nível"] -= 3
        
        if INVENTÁRIO["nível"] > 0: #verificando se está vivo
            print("")
            mapa_navio = {
                (0, 4): "X",
                (1, 3): "N",
                (2, 1): "N",
                (2, 2): "N",
                (3, 3): "N",
                (4, 1): "V",
            }
            
            posicao_atual = [[0, 0], "simbolo"]
            
            while posicao_atual[1] != "X":
                direcao = input()
                posicao_atual[0] = movimentacao(direcao, posicao_atual[0])
                posicao_atual[1] = mapa_navio.get((posicao_atual[0][0], posicao_atual[0][1]), "0")
                xp, mensagem = coleta(posicao_atual[1])
                INVENTÁRIO["nível"] += xp
                if mensagem != "":
                    print(mensagem)
            
            tem_requisitos = False
            if INVENTÁRIO["nível"] >= 5 and (len(INVENTÁRIO["magias"]) >= 2 or "Varinha de Gelo" in INVENTÁRIO["magias"]):
                tem_requisitos = True
                
            print("Polar Knight! O que você está fazendo aqui?")
            print("Como pode trair nosso juramento?")
            batalha = enfrentar("Polar Knight", INVENTÁRIO, INVENTÁRIO["nível"], tem_requisitos)
            if batalha == True:
                print("")
                print("======== TORRE DO DESTINO ========")
                print("Finalmente, aqui de novo…")
                print(f"ANTES - pás: {INVENTÁRIO['itens']['pás']}")
                for i in range(len(INVENTÁRIO['itens']['pás'])):
                    INVENTÁRIO['itens']['pás'].pop()
                INVENTÁRIO['itens']['pás'].append("coragem do cavaleiro")
                print(f"DEPOIS - pás: {INVENTÁRIO['itens']['pás']}")
                print("Perdi minhas pás, mas não posso recuar, agora é tudo ou nada!")

                encantamento  = ""
                while encantamento  != "Droga, não tenho mais nada de mana!":
                    encantamento = input()
                    if encantamento != "Droga, não tenho mais nada de mana!":
                        print("Não posso recuar de jeito nenhum! Irei superar meus limites aqui e agora!")
                        lista_frase = encantamento.split()
                        if "morte" in lista_frase:
                            INVENTÁRIO["nível"] -= 2
                        elif "magia" in lista_frase or "feitiço" in lista_frase:
                            INVENTÁRIO["nível"] -= 1
                
                vivo = False
                if INVENTÁRIO["nível"] > 0:
                    print("Minha amada! Finalmente pude revê-la e livrá-la desta terrível maldição!")
                    print("Vamos embora deste lugar amaldiçoado!\n")
                    vivo = True
                
                relatorio_final(vivo, INVENTÁRIO["troféus"], INVENTÁRIO["magias"], INVENTÁRIO["itens"]["pás"])
            else:
                relatorio_final(False, INVENTÁRIO["troféus"], INVENTÁRIO["magias"], INVENTÁRIO["itens"]["pás"])
            
        else:
            relatorio_final(False, INVENTÁRIO["troféus"], INVENTÁRIO["magias"], INVENTÁRIO["itens"]["pás"])
    
    else:
        relatorio_final(False, INVENTÁRIO["troféus"], INVENTÁRIO["magias"], INVENTÁRIO["itens"]["pás"])

else: #caso não exista feitiço ele morre
    relatorio_final(False, INVENTÁRIO["troféus"], INVENTÁRIO["magias"], INVENTÁRIO["itens"]["pás"])