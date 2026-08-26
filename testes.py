#fase 1
perigo = 0
string_fase1 = input()
tempo_decorrido = len(string_fase1) * 5

tipoEstrutura = ""

ferro = False
ouro = False
perolas = False
blaze = False
cama = False
usouCama = False
conseguiu = False
luta = False

print("Byte: Au! Vou conseguir esse ovo!!")

if string_fase1.isupper():
    perigo += 30
else:
    perigo += 10

if "monstros" in string_fase1.lower():
    perigo += 25
    tempo_decorrido += 20
    print("Você não pode dormir agora, há monstros por perto.")
    if "4" in string_fase1:
        perigo *= 2
        print("Byte desbloqueou a conquista: [Caçador de Monstros]")

elif "ferro" in string_fase1.lower():
    perigo -= 15
    perigo = abs(perigo)
    tempo_decorrido += 5
    ferro = True
    print("Byte desbloqueou a conquista: [A Idade do Ferro]")

if ferro and "diamante" in string_fase1.lower():
        perigo -= 40
        perigo = abs(perigo)
        print("Byte desbloqueou a conquista: [Diamantes!]")
else:
    tempo_decorrido += 15

if ferro and "ouro" in string_fase1.lower():
    tempo_decorrido += 10
    ouro = True
else:
    tempo_decorrido += 5

if perigo < 100:
    if "estrutura" in string_fase1.lower():
        tipoEstrutura = input()
        if "vila" in tipoEstrutura.lower():
            print("Byte desbloqueou a conquista: [Negócio Fechado!]")
            tempo_decorrido += 10
            cama = True
        elif "templo" in tipoEstrutura.lower():
            perigo += 100
            if perigo > 100:
                print("Byte desbloqueou a conquista: [À beira da Morte]")
        elif "mansao" in tipoEstrutura.lower():
            perigo -= 150
            perigo = abs(perigo)
            tempo_decorrido += 40
        elif "camara" in tipoEstrutura.lower():
            print("Byte desbloqueou a conquista: [Minecraft: Jogos Vorazes]")
            tempo_decorrido += 60
            perigo += 50
        print(f"Byte: Ufa, finalmente acabei, demorei apenas {tempo_decorrido} minutos, vamos ao Nether!")
    
    #fase2     
    if perigo < 100:
        if "portal" not in tipoEstrutura.lower():
            tempo_decorrido += 5
            print("Byte desbloqueou a conquista: [Entrando numa fria]")
        perigo += 30
        print("Byte desbloqueou a conquista: [O buraco é mais embaixo]")
        if perigo < 100:
            n1 = float(input())
            n2 = float(input())
            soma = n1 + n2
            inteiro = soma == int(soma)
            if soma:
                perolas = True
            else:
                print("Byte desbloqueou a conquista: [Meu precioso!]")
                if ouro:
                    perigo += 10
                    
                else:
                    perigo += 20
                    tempo_decorrido += 30
            if perigo < 100:
                resultado_blaze = input()
                if resultado_blaze.isnumeric():
                    if 1 <= int(resultado_blaze) <= 12:
                        tempo_decorrido += 20
                    elif int(resultado_blaze) > 12:
                        tempo_decorrido += 10
                    else:
                        tempo_decorrido += 30
                        perigo += 40 
                else:
                    tempo_decorrido += 30
                    perigo += 40        
                blaze = True
                
                #fase3
                if perigo < 100:
                    perigo -= 20
                    perigo = abs(perigo)
                    x = int(input())
                    z = int(input())
                    dist = int((((100 - x) ** 2) + ((200 - z) ** 2)) ** 0.5)
                    print(f"Byte: Estou a {dist} blocos da Stronghold!")
                    tempo_decorrido += dist * 2
                    perigo += 30
                    if perigo < 100:
                        print("Byte desbloqueou a conquista: [É o fim?]")
                        if tempo_decorrido < 300:
                            if cama: #caso ele tenha camas
                                perigo -= 30
                                print("Byte: Como eu amo o [Design Intencional do Jogo]!")
                                usouCama = True
                                conseguiu = True
                            else:
                                if tempo_decorrido > 180:
                                    print("Troia desbloqueou a conquista: [É o fim?]")
                                    luta = True
                                    perigo += 10
                                    if perigo < 100:
                                        n_flechas = int(input())
                                        n_alvos = int(input())
                                        
                                        if n_alvos == 1 and n_flechas == 0: #ficar de olho nisso
                                            print("Byte: Troia já destruiu todos os cristais, agora é só o Dragão...")
                                        if n_alvos == 1 and n_flechas == 1:
                                            print("Byte: Uma flecha, Uma chance.")
                                        
                                        divisao = n_flechas/n_alvos
                                        if divisao != int(divisao):
                                            print("Byte: Droga! Não tenha flechas suficientes, Troia vai ganhar...")
                                        if divisao > 0:
                                            tempo_decorrido += 10 #aqui deu certo
                                            conseguiu = True
                                            print("Byte desbloqueou a conquista: [Liberte o End]")
                                        else:
                                            tempo_decorrido += 20
                                elif tempo_decorrido < 180:
                                    conseguiu = True
                                    print("Byte desbloqueou a conquista: [Liberte o End]")
                                    tempo_decorrido += 5
                        else:
                            print("Troia desbloqueou a conquista: [Liberte o End]")
                        
                        if conseguiu:
                            if not usouCama:
                                print("Byte desbloqueou a conquista: [A nova geração]")
                            print("Byte: Aauauau! O ovo é meu! que rolem os créditos!")
                        else:
                            print("Byte: auu.... Não consegui pegar o ovo...")                     
                            
                            
else:
    print("Byte foi morto.")
    
print("")
print("🚨Avaliação de nível de perigo:")
if perigo < 30:
    print("Passeio no Parque.")
elif 30 <= perigo < 70:
    print("Jornada Complicada.")
elif 70 <= perigo < 100:
    print("Aventura Perigosa.")
elif perigo == 100:
    if luta:
        print("Odisseia de Byte.")
    else:
        print("Letal.")

print(" ")
hora = int(tempo_decorrido/60)
minutos = int((tempo_decorrido - hora) * 60)
print(f"Timer: {hora} h e {minutos} minutos")  
    