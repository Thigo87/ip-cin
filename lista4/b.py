def selecionar_personagem(nome):
    if nome == "Cavaleiro":
        return 55
    elif nome == "Paladino":
        return 80
    elif nome == "Sacerdotisa":
        return 60
    elif nome == "Necromante":
        return 40
    elif nome == "Assassino":
        return 45
    elif nome == "Bruxa":
        return 50

def movimentar(posicao_atual, movimento):
    linha = posicao_atual[0]
    coluna = posicao_atual[1]
    passo = False
    
    if movimento == "<":
        if coluna > 0:
            coluna -= 1
            passo = True
    elif movimento == ">":
        if coluna < 4:
            coluna += 1
            passo = True
    elif movimento == "^":
        if linha > 0:
            linha -= 1
            passo = True
    elif movimento == "v":
        if linha < 4:
            linha += 1
            passo = True
    
    return [[linha, coluna], passo]

def aplicar_efeito_sala(sala, hp, hp_max):
    if sala == "+":
        if hp + 20 > hp_max:
            return [hp_max - hp, False, True]
        else:
            return [20, False, True]
    elif sala == "c":
        if hp - 15 > 0:
            return [-15, False, True]
        else:
            return [-15, False, False]
    elif sala == "@":
        if hp - 25 > 0:
            return [-25, True, True]
        else:
            return [-25, False, False]
    else:
        return [0, False, True]

print("A jornada pela Pedra Mágica tem início! O destino do reino está selado, e esta guerra finalmente encontrará o seu fim.")
print("")

pedra_magica = False
vivo = True

personagem = input()
print(f"O(A) {personagem} é o(a) herói(na) lendário(a) escolhido(a)!")
hp = selecionar_personagem(personagem)
hp_max = hp
mapa = []

for i in range(5):
    linha = input()
    mapa.append(linha.split())

direcoes = input()
posicao_atual = [0,0]
passos = 0

for i in direcoes:
    if vivo:
        if hp != 0 and not pedra_magica and vivo:
            movimento = movimentar(posicao_atual, i)
            posicao_atual = movimento[0]
            if movimento[1] == True:
                passos += 1
            resultado_efeito = aplicar_efeito_sala(mapa[posicao_atual[0]][posicao_atual[1]], hp, hp_max)
            hp += resultado_efeito[0]
            pedra_magica = resultado_efeito[1]
            vivo = resultado_efeito[2]
            if not pedra_magica and hp > 0 and mapa[posicao_atual[0]][posicao_atual[1]] == 'c' and vivo:
                print(f"O(A) {personagem} prevalece no combate, mantendo-se firme com {hp} HP!")
            if pedra_magica and hp > 0 and vivo:
                print(f"A profecia se cumpriu e a paz reina mais uma vez!\nCruzando as profundezas da masmorra em {passos} passos de pura bravura, o(a) nosso(a) herói(na) ergue-se triunfante com {hp} HP.")
        
if hp <= 0 and not pedra_magica:  
    print("Ainda não é o fim! A jornada continua…")
    print("")
    novo_mapa = []
    for i in range(len(mapa)):
        nova_linha = []
        for j in mapa:
            nova_linha.append(j[i])
        novo_mapa.append(nova_linha)
        
    novo_personagem = input()
    print(f"O(A) {novo_personagem} é o(a) herói(na) lendário(a) escolhido(a)!")
    hp = selecionar_personagem(novo_personagem)
    hp_max = hp
    novas_direcoes = input()
    posicao_atual = [0,0]
    passos = 0
    
    vivo = True
    for i in direcoes:
        if vivo:
            if hp != 0 and not pedra_magica:
                movimento = movimentar(posicao_atual, i)
                posicao_atual = movimento[0]
                if movimento[1] == True:
                    passos += 1
                resultado_efeito = aplicar_efeito_sala(novo_mapa[posicao_atual[0]][posicao_atual[1]], hp, hp_max)
                hp += resultado_efeito[0]
                pedra_magica = resultado_efeito[1]
                vivo = resultado_efeito[2]
                if not pedra_magica and hp > 0 and novo_mapa[posicao_atual[0]][posicao_atual[1]] == 'c' and vivo:
                            print(f"O(A) {novo_personagem} prevalece no combate, mantendo-se firme com {hp} HP!")
                if pedra_magica and hp > 0 and vivo:
                            print(f"A profecia se cumpriu e a paz reina mais uma vez!\nCruzando as profundezas da masmorra em {passos} passos de pura bravura, o(a) nosso(a) herói(na) ergue-se triunfante com {hp} HP.")
                
    if not vivo:            
        print("Sem heróis. Sem esperança. O Reino caiu.")