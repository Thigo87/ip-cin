print("Byte: Au! Vou conseguir esse ovo!!")

#primeira fase
perigo = 0
string_fase1 = input()
timer = len(string_fase1) * 5

morto = False
ferro = False
diamantes = False
lingotes = False
camas = False
portal = False
totem = False
perolas = False
troia = False
pegouOvo = False

estrutura = ""

if string_fase1.isupper():
    perigo += 30
else:
    perigo += 10
    
if "monstros" in string_fase1.lower():
    print("Você não pode dormir agora, há monstros por perto.")
    perigo += 25
    timer += 20
    if "4" in string_fase1:
        print("Byte desbloqueou a conquista: [Caçador de Monstros]")
        perigo *= 2

if "ferro" in string_fase1.lower():
    print("Byte desbloqueou a conquista: [A Idade do Ferro]")
    ferro = True
    perigo -= 15
    timer += 5
    
if "diamante" in string_fase1.lower():
    if ferro:
        print("Byte desbloqueou a conquista: [Diamantes!]")
        diamantes = True
        perigo -= 40
    else:
        timer += 15

if "ouro" in string_fase1.lower():
    if ferro:
        lingotes = True
        timer += 10
    else:
        timer += 5

if "estrutura" in string_fase1.lower():
    estrutura = input()
    if "vila" in estrutura.lower():
        print("Byte desbloqueou a conquista: [Negócio Fechado!]")
        camas = True
        timer += 10
    if "portal" in estrutura.lower():
        portal = True
    if "templo" in estrutura.lower():
        perigo += 100
    if "mansao" in estrutura.lower():
        if perigo > 100:
            print("Byte desbloqueou a conquista: [À beira da Morte]")
        totem = True
        perigo -= 150
        timer += 40
    if "camara" in estrutura.lower():
        print("Byte desbloqueou a conquista: [Minecraft: Jogos Vorazes]")
        timer += 60
        perigo += 50

perigo = abs(perigo)

if perigo < 100:
    print(f"Byte: Ufa, finalmente acabei, demorei apenas {timer} minutos, vamos ao Nether!")
    
    #segunda fase
    if not portal:
        print("Byte desbloqueou a conquista: [Entrando numa fria]")
        timer += 5
    
    print("Byte desbloqueou a conquista: [O buraco é mais embaixo]")
    perigo += 30
    
    n1 = float(input())
    n2 = float(input())
    
    if n1 + n2 == int(n1 + n2):
        perolas = True
    else:
        if lingotes:
            print("Byte desbloqueou a conquista: [Meu precioso!]")
            perigo += 10
        else:
            perigo += 20
            timer += 30
        perolas = True
    
    resultado_blaze = input()
    if resultado_blaze.isnumeric():
        if 1 <= float(resultado_blaze) <= 12:
            timer += 20
        elif float(resultado_blaze) > 12:
            timer += 10
    else:
        timer += 30
        perigo += 40
    
    perigo = abs(perigo)
    #terceira fase
    if perigo < 100:
        perigo -= 20
        x = int(input())
        z = int(input())
        dist = (((100 - x) ** 2) + ((200 - z) ** 2)) ** 0.5
        print(f"Byte: Estou a {int(dist)} blocos da Stronghold!")
        timer += dist * 2

        perigo = abs(perigo)
        if perigo < 100:
            print("Byte desbloqueou a conquista: [É o fim?]")
            perigo += 30
            if timer > 300:
                print("Troia desbloqueou a conquista: [Liberte o End]")
            elif 180 <= timer <= 300:
                print("Troia desbloqueou a conquista: [É o fim?]")
                if camas: #não vai desbloquear liberte o end
                    print("Byte: Como eu amo o [Design Intencional do Jogo]!")
                    perigo -= 30
                else:
                    perigo += 10
                    n_flechas = int(input())
                    n_alvos = int(input())
                    divisao = n_flechas/n_alvos
                    
                    if n_alvos == 1:
                        print("Byte: Troia já destruiu todos os cristais, agora é só o Dragão...")
                    if n_alvos == 1 and n_flechas ==1:
                        print("Byte: Uma flecha, Uma chance.")
                    
                    if divisao > 0 and divisao == int(divisao):
                        troia = True
                        print("Byte desbloqueou a conquista: [Liberte o End]")
                        pegouOvo = True
                        timer += 10
                    else:
                        print("Byte: Droga! Não tenha flechas suficientes, Troia vai ganhar...")
                        timer += 20
            elif timer < 180:
                if camas:
                    print("Byte: Como eu amo o [Design Intencional do Jogo]!")
                    perigo -= 30
                else:
                    print("Byte desbloqueou a conquista: [Liberte o End]")
                    timer += 5
                    pegouOvo = True
        else:
            print("Byte foi morto.")
            morto = True
        
    else:
        print("Byte foi morto.")
        morto = True
        
else:
    print("Byte foi morto.")
    morto = True

if morto:
    print("Byte foi morto.")

if pegouOvo:
    print("Byte desbloqueou a conquista: [A nova geração]")
    print("Byte: Aauauau! O ovo é meu! que rolem os créditos!")
else:
    print("Byte: auu.... Não consegui pegar o ovo...")

print("")
print("🚨Avaliação de nível de perigo: ")

if perigo == 100 or troia:
    print("Odisseia de Byte.")
elif perigo < 30:
    print("Passeio no Parque.")
elif 30 <= perigo < 70:
    print("Jornada Complicada.")
elif 70 <= perigo < 100:
    print("Aventura Perigosa.")
elif perigo > 100:
    print("Letal.")

print("")
hora = int(timer/60)
minutos = int(timer - (hora*60))
print(f"Timer: {hora} h e {minutos} minutos") 