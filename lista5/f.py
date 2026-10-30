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
            inventario.update({item : {"tipo" : tipo, "poder" : int(poder_do_item)}})
    
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

print("Boa noite a todos!! Sejam bem vindos ao reino de Cinland. A aventura será longa, mas a gloria é eterna!!\nVamos as apresentações.")
print("")
quantidade_aventureiros = int(input()) #input da quantidade de aventureiros

while quantidade_aventureiros < 1 or quantidade_aventureiros > 4:
    print("Não tem toda essa gente pra jogar não.") #mensagem de erro
    quantidade_aventureiros = int(input()) #pede o input novamente

for i in range(quantidade_aventureiros): #loop de acordo com a quantidade de aventureiros
    nome, classe = input().split() #recebe o input do nome e da classe do personagem i
    personagens.append(classe)
    
    #verificando os inputs e separando de acordo com a classe
    if classe == "B":
        bardo.update({"nome" : nome, "inventario":{}})
        frase = ""
        while frase != "pronto":
            frase = input()
            if frase != "pronto":
                bardo["inventario"].update(montagem_inventario(frase))

        itens = ""
        counter = 0
        for item in bardo["inventario"]:
            itens += f"{item} [{bardo['inventario'][item]['tipo']}, {bardo['inventario'][item]['poder']}], "
            counter += 1

        if counter != 0:
            print(f"{nome} (Bardo): {itens[:(len(itens) - 2)]}")     
        else:
            print(f"{nome} (Bardo): sem itens")

    elif classe == "G":
        guerreiro.update({"nome" : nome, "inventario":{}})
        frase = ""
        while frase != "pronto":
            frase = input()
            if frase != "pronto":
                guerreiro["inventario"].update(montagem_inventario(frase))

        itens = ""
        counter = 0
        for item in guerreiro["inventario"]:
            itens += f"{item} [{guerreiro['inventario'][item]['tipo']}, {guerreiro['inventario'][item]['poder']}], "
            counter += 1

        if counter != 0:
            print(f"{nome} (Guerreiro): {itens[:(len(itens) - 2)]}")     
        else:
            print(f"{nome} (Guerreiro): sem itens")
                
    elif classe == "L":
        ladino.update({"nome" : nome, "inventario":{}})
        frase = ""
        while frase != "pronto":
            frase = input()
            if frase != "pronto":
                ladino["inventario"].update(montagem_inventario(frase))

        itens = ""
        counter = 0
        for item in ladino["inventario"]:
            itens += f"{item} [{ladino['inventario'][item]['tipo']}, {ladino['inventario'][item]['poder']}], "
            counter += 1

        if counter != 0:
            print(f"{nome} (Ladino): {itens[:(len(itens) - 2)]}")     
        else:
            print(f"{nome} (Ladino): sem itens")

    elif classe == "M":
        mago.update({"nome" : nome, "inventario":{}})
        frase = ""
        while frase != "pronto":
            frase = input()
            if frase != "pronto":
                mago["inventario"].update(montagem_inventario(frase))

        itens = ""
        counter = 0
        for item in mago["inventario"]:
            itens += f"{item} [{mago['inventario'][item]['tipo']}, {mago['inventario'][item]['poder']}], "
            counter += 1

        if counter != 0:
            print(f"{nome} (Mago): {itens[:(len(itens) - 2)]}")     
        else:
            print(f"{nome} (Mago): sem itens")

print("Grupo completamente apresentado, espero que todos estejam preparados para o que estar por vir.")
print("")
print("Ao passa pelo arco de pedras, vocês encontram um lugar silencioso, com um odor nada agradável e um frio sem igual. Um calafrio na espinha os chama a recuar, mas a jornada começa aqui. Bem vindos a Dungeon do Grad5.")
#criando o mapa
mapa = []
qt_linhas_colunas = int(input())

for linha in range(qt_linhas_colunas):
    linha = []
    linha_da_matriz = input()
    for item in linha_da_matriz.split():
        linha.append(int(item))
    mapa.append(linha)


#configurando a posição inicial e o valor dessa posição
posicao_atual = [0, 0]
valor_posicao = 0
#loop da movimentação
while valor_posicao != 99 and len(personagens) > 0:
    if valor_posicao == 0:
        print("Casa visitada: Entrada")        

    if ePrimo(valor_posicao): #caiu na armadilha
        tipo_armadilha = input()

        print("Casa visitada: Armadilha")

        if tipo_armadilha == "flechas": # se a armadilha for flecha
            if len(guerreiro) > 0: #verificando se há um guerreiro
                if "escudo de madeira" in guerreiro["inventario"]: #verificando se o guerreiro tem o escudo
                    print(f"O escudo de madeira de {guerreiro['nome']} protegeu o grupo.")
                    del guerreiro["inventario"]["escudo de madeira"] #se tiver, ele é usado
                
                else: #se não o último personagem é morto, caso ele não seja o bardo ou o bardo não tenha a poção de cura
                    ultimo_personagem = len(personagens) - 1
                    
                    if ultimo_personagem >= 0: #verificando se há personagens vivos
                        if personagens[ultimo_personagem] == "B":
                            print(f"{bardo['nome']} sacrificou-se pelo grupo.")
                            bardo = {}
                            personagens.pop()
                        elif personagens[ultimo_personagem] == "G":
                            if "B" in personagens:
                                print(f"{guerreiro['nome']} sacrificou-se pelo grupo.")
                                if "pocao de cura" not in bardo["inventario"]:
                                    guerreiro = {}
                                    personagens.pop()
                                else:
                                    del bardo["inventario"]["pocao de cura"]
                                    print(f"{bardo['nome']} usou a pocao de cura e salvou {guerreiro['nome']}.")
                            else:
                                print(f"{guerreiro['nome']} sacrificou-se pelo grupo.")
                                guerreiro = {}
                                personagens.pop()
                        elif personagens[ultimo_personagem] == "L":
                            if "B" in personagens:
                                print(f"{ladino['nome']} sacrificou-se pelo grupo.")
                                if "pocao de cura" not in bardo["inventario"]:
                                    ladino = {}
                                    personagens.pop()
                                else:
                                    del bardo["inventario"]["pocao de cura"]
                                    print(f"{bardo['nome']} usou a pocao de cura e salvou {ladino['nome']}.")
                            else:
                                print(f"{ladino['nome']} sacrificou-se pelo grupo.")
                                ladino = {}
                                personagens.pop()
                            
                        elif personagens[ultimo_personagem] == "M":
                            if "B" in personagens:
                                print(f"{mago['nome']} sacrificou-se pelo grupo.")
                                if "pocao de cura" not in bardo["inventario"]:
                                    mago = {}
                                    personagens.pop()
                                else:
                                    del bardo["inventario"]["pocao de cura"]
                                    print(f"{bardo['nome']} usou a pocao de cura e salvou {mago['nome']}.")
                            else:
                                print(f"{mago['nome']} sacrificou-se pelo grupo.")
                                mago = {}
                                personagens.pop()
            else:
                ultimo_personagem = len(personagens) - 1
                
                if ultimo_personagem >= 0: #verificando se há personagens vivos
                    if personagens[ultimo_personagem] == "B":
                        print(f"{bardo['nome']} sacrificou-se pelo grupo.")
                        bardo = {}
                        personagens.pop()
                    elif personagens[ultimo_personagem] == "L":
                        if "B" in personagens:
                            print(f"{ladino['nome']} sacrificou-se pelo grupo.")
                            if "pocao de cura" not in bardo["inventario"]:
                                ladino = {}
                                personagens.pop()
                            else:
                                del bardo["inventario"]["pocao de cura"]
                                print(f"{bardo['nome']} usou a pocao de cura e salvou {ladino['nome']}.")
                        else:
                            print(f"{ladino['nome']} sacrificou-se pelo grupo.")
                            ladino = {}
                            personagens.pop()
                        
                    elif personagens[ultimo_personagem] == "M":
                        if "B" in personagens:
                            print(f"{mago['nome']} sacrificou-se pelo grupo.")
                            if "pocao de cura" not in bardo["inventario"]:
                                mago = {}
                                personagens.pop()
                            else:
                                del bardo["inventario"]["pocao de cura"]
                                print(f"{bardo['nome']} usou a pocao de cura e salvou {mago['nome']}.")
                        else:
                            print(f"{mago['nome']} sacrificou-se pelo grupo.")
                            mago = {}
                            personagens.pop()              
                
        elif tipo_armadilha == "beholder": #se a armadilha for o beholder
            if "L" in personagens: #verificando se o ladino está nos personagens
                if "bomba de fumaca" in ladino["inventario"]: #verificando se o ladino tem a bomba de fumaça
                    del ladino["inventario"]["bomba de fumaca"]
                    print(f"{ladino['nome']} usou a bomba de fumaça e o escaparam do Beholder.")
                else:
                    personagens = []
                    print("Entraram em uma sala que não deveriam. A ultima visão é tudo ficando vermelho e em um flash, tudo fica preto. Vocês tão mortos.")
            else:
                personagens = []
                print("Entraram em uma sala que não deveriam. A ultima visão é tudo ficando vermelho e em um flash, tudo fica preto. Vocês tão mortos.")

    if quadradoPerfeito(valor_posicao) and personagens != []: #sala de looting

        print("Casa visitada: Looting")
        print("Finalmente um descanso! Aproveitam as maravilhas presentes na sala.")
        if "L" in personagens:
            if "ferramentas de ladrao" in ladino["inventario"]:
                print(f"{ladino['nome']} arrombou o baú trancado!")
        
        itens_especiais = {"B" : "lira encantada", "G" : "martelo do trovao", "L" : "olho do abismo", "M" : "orbe arcano"} #Itens especiais e classes ideais
        codigo = {} #para a consulta da ordem lexicográfica
        personagens_vivos = personagens
        n = len(personagens_vivos)
        
        for i in range(n):
            for j in range(n - i - 1):
                if personagens_vivos[j] > personagens_vivos[j + 1]:
                    personagens_vivos[j], personagens_vivos[j + 1] = personagens_vivos[j + 1], personagens_vivos[j]
        
        for i in range(n):
            codigo.update({i : personagens_vivos[i]})
        
        item_especial, cod_inventario = input().split(" - ") #recebendo o input da sala
        
        calculo = int(cod_inventario) % n
        
        personagem_selecionado = codigo[calculo]
        
        classe_ideal = False
        
        if item_especial == itens_especiais[personagem_selecionado]: #verificando se o item vai combinar com a classe ideal
            classe_ideal = True
        nome = ""
        classe = ""
        frase_classe = ""
        multiplicador = 1 #ajustando o multiplicador de acordo com a classe
        if classe_ideal:
            multiplicador += 1
            frase_classe = "O poder que esta em suas mãos é grandioso e parece chamar-lhe a glória eterna."
        else:
            multiplicador += 0.25
            frase_classe = "O poder é grande demais, você não consegue extrair o máximo dele."
        
        if personagem_selecionado == "B" and "B" in personagens: #ajustando o poder de cada item
            for item in bardo["inventario"]:
                bardo["inventario"][item]["poder"] *= multiplicador
                bardo["inventario"][item]["poder"] = int(bardo["inventario"][item]["poder"])
                nome = bardo['nome']
                classe = "Bardo"
        elif personagem_selecionado == "G" and "G" in personagens:
            for item in guerreiro["inventario"]:
                guerreiro["inventario"][item]["poder"] *= multiplicador
                guerreiro["inventario"][item]["poder"] = int(guerreiro["inventario"][item]["poder"])
                nome = guerreiro['nome']
                classe = "Guerreiro"
        elif personagem_selecionado == "L" and "L" in personagens:
            for item in ladino["inventario"]:
                ladino["inventario"][item]["poder"] *= multiplicador
                ladino["inventario"][item]["poder"] = int(ladino["inventario"][item]["poder"])
                nome = ladino['nome']
                classe = "Ladino"
        elif personagem_selecionado == "M" and "M" in personagens:
            for item in mago["inventario"]:
                mago["inventario"][item]["poder"] *= multiplicador
                mago["inventario"][item]["poder"] = int(mago["inventario"][item]["poder"])
                nome = mago['nome']
                classe = "Mago"
        
        print(f"{item_especial} foi para {nome} ({classe}).")
        print(frase_classe)
            
        if "L" in personagens: #verificando se há o ladino
            if "ferramentas de ladrao" in ladino["inventario"]: #verificando se ele tem as ferramentas no inventário
                item_especial, cod_inventario = input().split(" - ") #recebendo o input especial da sala
                del ladino["inventario"]["ferramentas de ladrao"] #deleta a ferramenta
                personagens_vivos = len(personagens)
                calculo = int(cod_inventario) % personagens_vivos
                
                personagem_selecionado = codigo[calculo]
                
                classe_ideal = False
                
                if item_especial == itens_especiais[personagem_selecionado]: #verificando se o item vai combinar com a classe ideal
                    classe_ideal = True
                
                nome = ""
                classe = ""
                frase_classe = ""
                multiplicador = 1 #ajustando o multiplicador de acordo com a classe
                if classe_ideal:
                    multiplicador += 1
                    frase_classe = "O poder que esta em suas mãos é grandioso e parece chamar-lhe a glória eterna."
                else:
                    multiplicador += 0.25
                    frase_classe = "O poder é grande demais, você não consegue extrair o máximo dele."
                
                if personagem_selecionado == "B": #ajustando o poder de cada item
                    for item in bardo["inventario"]:
                        bardo["inventario"][item]["poder"] *= multiplicador
                        bardo["inventario"][item]["poder"] = int(bardo["inventario"][item]["poder"])
                        nome = bardo['nome']
                        classe = "Bardo"
                elif personagem_selecionado == "G":
                    for item in guerreiro["inventario"]:
                        guerreiro["inventario"][item]["poder"] *= multiplicador
                        guerreiro["inventario"][item]["poder"] = int(guerreiro["inventario"][item]["poder"])
                        nome = guerreiro['nome']
                        classe = "Guerreiro"
                elif personagem_selecionado == "L":
                    for item in ladino["inventario"]:
                        ladino["inventario"][item]["poder"] *= multiplicador
                        ladino["inventario"][item]["poder"] = int(ladino["inventario"][item]["poder"])
                        nome = ladino['nome']
                        classe = "Ladino"
                elif personagem_selecionado == "M":
                    for item in mago["inventario"]:
                        mago["inventario"][item]["poder"] *= multiplicador
                        mago["inventario"][item]["poder"] = int(mago["inventario"][item]["poder"])
                        nome = mago['nome']
                        classe = "Mago"

                print(f"{item_especial} foi para {nome} ({classe}).")
                print(frase_classe)

    if valor_posicao != 0 and not ePrimo(valor_posicao) and not quadradoPerfeito(valor_posicao) and len(personagens) > 0:
        print("Casa visitada: Sala Comum")

    posicao_atual, valor_posicao = movimentacao(mapa, posicao_atual)

if len(personagens) > 0:
    print("Casa visitada: Saída")
    print("Vocês finalmente saem das cavernas escuras e frias. Mas não parece chegar em um lugar melhor.")
    print("")
else:
    print("Os sonhos e objetivos de todos são deixados no chão do Grad5. Nenhum de vocês restou. A glória nunca será alcançada!")

#final boss
if personagens != []: #verificando se há personagens vivos
    print("O lugar é silencioso. Até que, de repente, um rugido é ouvido. Uma criatura surge das sombras: o temido TarraByte!")
    final_boss = {"hp" : 0, "ca" : 0}

    HP_monstro, CA_monstro = input().split()
    final_boss["hp"] = int(HP_monstro)
    final_boss["ca"] = int(CA_monstro)
    
    ataques = {}
    for aventureiro in range(len(personagens)): #para cada aventureiro vivo
        iniciativa, ataque = input().split()
        ataques.update({personagens[aventureiro] : {"iniciativa" : int(iniciativa), "ataque" : int(ataque)}}) #atualiza o dicionário de ataques
        
    ataques_em_ordem = {} #criando o dicionário para ordenar os ataques
    iniciativas = [] #lista para receber os valores das iniciativas
    
    for personagem in ataques:
        iniciativas.append(ataques[personagem]["iniciativa"])
    
    #bubble sorting -> ordenando os ataques
    n = len(iniciativas)
    
    for i in range(n):
        for j in range(n - i - 1):
            if iniciativas[j] < iniciativas[j + 1]:
                iniciativas[j], iniciativas[j + 1] = iniciativas[j + 1], iniciativas[j]

    for valor in iniciativas:
        for personagem in ataques:
            if valor == ataques[personagem]["iniciativa"]:
                ataques_em_ordem.update({personagem : ataques[personagem]})

    ordem = ""

    for personagem in ataques_em_ordem:
        if personagem == "B":
            ordem += f"{bardo['nome']}, "
        elif personagem == "M":
            ordem += f"{mago['nome']}, "
        elif personagem == "G":
            ordem += f"{guerreiro['nome']}, "
        elif personagem == "L":
            ordem += f"{ladino['nome']}, "

    ordem = ordem[:(len(ordem) - 2)]

    print(f"Ordem de iniciativa: {ordem}")

    alaude = False
    if "B" in personagens:
        if "alaude" in bardo["inventario"]:
            alaude = True

    bonus = 0
    vez_bardo = False
    
    for ataque in ataques_em_ordem: #fazendo os ataques
        critico = False
        if ataques_em_ordem[ataque]["ataque"] == 20:
            critico = True
        if alaude and ataque == "B": #verificando se o alaude está no inventário e é o bardo
            print(f"{bardo['nome']} inspirou o grupo.")
            bonus = 2
            vez_bardo = True
        else: #se não for o bardo ou não houver o alaude
            if vez_bardo: #caso tenha o alaude e o bardo já tenha passado
                if ataque == "G" or ataque == "L": #se for ladino ou guerreiro
                    ataques_em_ordem[ataque]['ataque'] += bonus

        if ((ataques_em_ordem[ataque]["ataque"] >= final_boss["ca"]) or critico) and final_boss["hp"] > 0:
            nome = ""
            arma = ""
            poder = 0

            if not alaude and ataque == "B":
                nome = bardo["nome"]
                for item in bardo["inventario"]:
                    if bardo["inventario"][item]['tipo'] == 'arma':
                        if bardo["inventario"][item]['poder'] > poder:
                            poder = bardo["inventario"][item]['poder']
                            arma = item

                if critico:
                    poder *= 2

            elif ataque == "G":
                nome = guerreiro["nome"]
                racao = False
                for item in guerreiro["inventario"]:
                    if guerreiro["inventario"][item]['tipo'] == 'arma':
                        if guerreiro["inventario"][item]['poder'] > poder:
                            poder = guerreiro["inventario"][item]['poder']
                            arma = item
                    if item == "racao de viagem":
                        poder += guerreiro["inventario"][item]['poder']
                        racao = True

                if racao:
                    del guerreiro["inventario"]["racao de viagem"]

                if critico:
                    poder *= 2

            elif ataque == "L":
                nome = ladino["nome"]
                for item in ladino["inventario"]:
                    if ladino["inventario"][item]['tipo'] == 'arma':
                        if ladino["inventario"][item]['poder'] > poder:
                            poder = ladino["inventario"][item]['poder']
                            arma = item
                        
                if critico:
                    poder *= 2

            elif ataque == "M":
                nome = mago["nome"]
                pergaminho = False
                for item in mago["inventario"]:
                    if mago["inventario"][item]['tipo'] == 'arma':
                        if mago["inventario"][item]['poder'] > poder:
                            poder = mago["inventario"][item]['poder']
                            arma = item

                    if item == "pergaminho oculto":
                        poder += mago["inventario"][item]['poder']
                        pergaminho = True

                if pergaminho:
                    del mago["inventario"]["pergaminho oculto"]

                if critico:
                    poder *= 2

            final_boss["hp"] -= poder #ataque
            
            if critico:
                print(f"{nome} acertou um critico e causou {poder} de dano.")
            else:
                print(f"{nome} acertou e causou {poder} de dano.")

            if final_boss["hp"] <= 0:
                print(f"O TarraByte foi derrotado por {nome}!")

        else:
            if final_boss["hp"] > 0:
                if ataque == "B" and not alaude:
                    print(f"{bardo['nome']} errou o ataque.")
                if ataque == "M":
                    print(f"{mago['nome']} errou o ataque.")
                if ataque == "G":
                    print(f"{guerreiro['nome']} errou o ataque.")
                if ataque == "L":
                    print(f"{ladino['nome']} errou o ataque.")

    if final_boss["hp"] > 0:
        print(f"O TarraByte sobreviveu com {final_boss['hp']} de HP e obliterou o grupo. Fim da aventura.")