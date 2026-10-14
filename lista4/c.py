baralho = []
itens = []
totens = []

chefes = 0

canideos = ["lobo", "coiote", "cachorro"]
insetos = ["louva-a-deus", "abelha", "formiga"]
aves = ["corvo", "urubu", "pardal"]
cervideos = ["antilocapra", "alce", "caribu"]
repteis = ["rã", "tartaruga", "víbora"]

def montar_baralho(baralho):
    carta = ""
    if carta != "FIM":
        carta = input()
        if carta != "FIM":
            baralho.append(carta)
            return True
        else:
            return False    

def itens_e_totens(item):
    totem = False
    
    if item.lower() =="totem":
        totem = True
    
    if len(itens) < 3:
        if totem:
            classe_totem = input()
            totens.append(classe_totem)
            print(f"Totem ativo: {classe_totem.capitalize()}")
        else:
            itens.append(item)
    else:
        print("Inventario cheio")

def calculo_do_coeficiente_carta(carta):
    cartas_raras = ["urayuli", "louva-a-deus rei", "ameba", "tubarão", "urso"]
    coeficiente = 0
    if "filhote de" in carta.lower() or "ovo de" in carta.lower():
        coeficiente += 5
    elif carta.lower() in cartas_raras:
        coeficiente += 20
    else:
        if "pele" not in carta.lower():
            coeficiente += 10

    return coeficiente

def calculo_do_coeficiente_itens_e_totens(baralho, itens, totens):   
    itens_ativos = []
    coeficiente = 0
    for item in itens:
        if len(itens_ativos) < 3 or itens_ativos != itens:
            itens_ativos.append(item)
        
    for item in itens_ativos:
        for char in item:
            coeficiente += 1 if char != ' ' else 0
    if len(totens) > 0:
        totem_ativo = totens[0]
    else:
        totem_ativo = "0"
    if totem_ativo.lower() == "canideos":
        for nome in canideos:
            for carta in baralho:
                if nome in carta.lower():
                        coeficiente += calculo_do_coeficiente_carta(carta)
    elif totem_ativo.lower() == "insetos":
            for nome in insetos:
                for carta in baralho:
                    if nome in carta.lower():
                        coeficiente += calculo_do_coeficiente_carta(carta)
    elif totem_ativo.lower() == "aves":
            for nome in aves:
                for carta in baralho:
                    if nome in carta.lower():
                        coeficiente += calculo_do_coeficiente_carta(carta)
    elif totem_ativo.lower() == "cervideos":
            for nome in cervideos:
                for carta in baralho:
                    if nome in carta.lower():
                        coeficiente += calculo_do_coeficiente_carta(carta)
    elif totem_ativo.lower() == "repteis":
            for nome in repteis:
                for carta in baralho:
                    if nome in carta.lower():
                        coeficiente += calculo_do_coeficiente_carta(carta)
                        
    return coeficiente
       
def simular_batalha(chefe, coeficiente, baralho, itens, totens):
    boss_hp = 0
    if chefe == "Garimpeiro":
        print("Garimpeiro - É o Garimpeiro! OPA!")
        coeficiente = coeficiente // 2
        boss_hp = 40
        if coeficiente <= boss_hp:
            print("Garimpeiro - Mais ouro pra mim!") if coeficiente < boss_hp else print("Leshy - A fome se instala. Que lástima... chegou a hora da sua ruína.")
            return 0
        else:
            print("Garimpeiro - Oxe!")
            return coeficiente
    elif chefe == "Pescador":
        print("Pescador - Eu sou o Pescador. Quer pescar?")
        boss_hp = 90
        denominador = len(baralho)
        boss_hp += coeficiente // denominador
        if coeficiente <= boss_hp:
            print("Pescador - Hum. Vai pescar.") if coeficiente < boss_hp else print("Leshy - A fome se instala. Que lástima... chegou a hora da sua ruína.")
            return 0
        else:
            print("Pescador - Vai pescar...")
            return coeficiente
    elif chefe == "Comerciante":
        boss_hp = 160
        print("Comerciante - Vamos negociar.")
        for carta in baralho:
            if "pele" in carta.lower():
                boss_hp -= 10
                coeficiente += 10
        if coeficiente <= boss_hp:
            print("Comerciante - Você vai virar uma pele deslumbrante.") if coeficiente < boss_hp else print("Leshy - A fome se instala. Que lástima... chegou a hora da sua ruína.")
            return 0
        else:
            print("Comerciante - Hmm... muito bem.")
            return coeficiente

def inventario(itens):
    inventario = ""
    for item in itens:
        inventario += f'{item}, '
    inventario = inventario[0:(len(inventario) - 2)]
    return inventario

print("Leshy - Outro desafiante. Já faz tanto tempo...")
#Matagal
coeficiente_total = 0
print("Leshy - O sol banha os abetos sonolentos, você adentrou o... matagal.")
#montando o baralho
processo = True
counter = 0
while processo:
    counter += 1
    processo = montar_baralho(baralho)
    
print(f"{counter - 1} cartas foram adicionadas ao baralho")

for carta in baralho:
    coeficiente_total += calculo_do_coeficiente_carta(carta)
#recebendo itens
item = ""
while item != "FIM":
    item = input()
    if item != "FIM":
        itens_e_totens(item)

print(f'Itens no inventario: {inventario(itens)}')

if len(totens) > 0:
    totens = totens[::-1]
coeficiente_total += calculo_do_coeficiente_itens_e_totens(baralho, itens, totens)
batalha = simular_batalha("Garimpeiro", coeficiente_total, baralho, itens, totens)
coeficiente_total = batalha
if batalha > 0:
    itens = []
    chefes += 1 
    #Charneca
    coeficiente_total = 0
    print("Leshy - O ar úmido é tomado pelo cheiro fétido de mofo e morte, você caminha cautelosamente até entrar na... charneca.")
    #montando o baralho
    processo = True
    counter = 0
    while processo:
        counter += 1
        processo = montar_baralho(baralho)
    
    print(f"{counter - 1} cartas foram adicionadas ao baralho")
    
    for carta in baralho:
        coeficiente_total += calculo_do_coeficiente_carta(carta)
    #recebendo itens
    item = ""
    while item != "FIM":
        item = input()
        if item != "FIM":
            itens_e_totens(item)
    
    print(f'Itens no inventario: {inventario(itens)}')
    if len(totens) > 0:
        totens = totens[::-1]
    coeficiente_total += calculo_do_coeficiente_itens_e_totens(baralho, itens, totens)
    batalha = simular_batalha("Pescador", coeficiente_total, baralho, itens, totens)
    coeficiente_total = batalha
    if batalha > 0:
        itens = []
        chefes += 1
        #Linha de neve
        coeficiente_total = 0
        print("Leshy - O alívio do ar fresco logo dá lugar a um arrepio álgido. Você escala até a... linha de neve.")
        #montando o baralho
        processo = True
        counter = 0
        while processo:
            counter += 1
            processo = montar_baralho(baralho)
            
        print(f"{counter - 1} cartas foram adicionadas ao baralho")    
        
        for carta in baralho:
            coeficiente_total += calculo_do_coeficiente_carta(carta)
        #recebendo itens
        item = ""
        while item != "FIM":
            item = input()
            if item != "FIM":
                itens_e_totens(item)
        
        print(f'Itens no inventario: {inventario(itens)}')
        if len(totens) > 0:
            totens = totens[::-1]
        coeficiente_total += calculo_do_coeficiente_itens_e_totens(baralho, itens, totens)
        batalha = simular_batalha("Comerciante", coeficiente_total, baralho, itens, totens)
        
        if batalha > 0:
            chefes += 1
            print("Leshy - A luz cálida da cabana atravessa o denso nevoeiro... seus infortúnios acabam aqui.")