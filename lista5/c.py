reliquias_lendarias = {"Espada Sagrada" : 15, "Arco Lendário" : 20, "Cajado Magistral" : 25}
rei_demonio = {"vida" : 100, "agilidade" : 32, "dano" : 25}
herois = {}
herois_tombados = []
herois_suficientes = False

print("As sombras avançam sobre o Reino Celeste... É chegada a hora de reunir os heróis dispostos a enfrentar o Rei Demônio!")

heroi_nome = ""
while heroi_nome != "FIM":
    heroi_nome = input()
    if heroi_nome != "FIM":
        atributos = input()
        atributos = atributos.split(" - ")
        vida = int(atributos[0].split()[1])
        agilidade = int(atributos[1].split()[1])
        arma = ""
        for i in range(len(atributos[2].split()[1::])):
          if i != len(atributos[2].split()[1::]) - 1:
            arma += f"{atributos[2].split()[1::][i]} "
          else:
            arma += f"{atributos[2].split()[1::][i]}"
        
        herois.update({heroi_nome : {"vida" : vida, "agilidade" : agilidade, "arma" : arma}})
        
if len(herois) < 3:
    print("Poucos atenderam ao chamado do reino... Sem ao menos três heróis para formar a resistência, o Reino Celeste parece condenado à ruína!")
else:
    herois_suficientes = True
    print("Os portões do castelo se abrem e os heróis marcham rumo ao campo de batalha. O confronto contra o Rei Demônio começa agora!")
    while rei_demonio["vida"] > 0 and len(herois) != len(herois_tombados):
        heroi_ataque = input()
        if heroi_ataque not in herois or heroi_ataque in herois_tombados:
            print("Nenhum herói com esse nome está no campo de batalha. O Rei Demônio aguarda impacientemente por seu próximo adversário!")
        else:
            if herois[heroi_ataque]["agilidade"] > rei_demonio["agilidade"]:
                if herois[heroi_ataque]["arma"] in reliquias_lendarias:
                    rei_demonio["vida"] -= reliquias_lendarias[herois[heroi_ataque]["arma"]]
                    print(f"{heroi_ataque} brandiu {herois[heroi_ataque]['arma']} contra o Rei Demônio e causou {reliquias_lendarias[herois[heroi_ataque]['arma']]} pontos de dano!")
                    if rei_demonio["vida"] > 0:
                        herois[heroi_ataque]["vida"] -= 25
                        print(f"O Rei Demônio avançou com suas garras infernais e atingiu {heroi_ataque}, causando 25 pontos de dano!")
                        if herois[heroi_ataque]["vida"] <= 0:
                            print(f"{heroi_ataque} tombou diante do poder do Rei Demônio!")
                            herois_tombados.append(heroi_ataque)
                    else:
                        print(f"Com um golpe decisivo, {heroi_ataque} derrota o Rei Demônio! Após uma longa batalha, o Reino Celeste está finalmente livre de sua ameaça!")
                else:
                    print("A arma do herói não possui poder suficiente para atravessar a aura sombria do Rei Demônio!")
                    if rei_demonio["vida"] > 0:
                        herois[heroi_ataque]["vida"] -= 25
                        print(f"O Rei Demônio avançou com suas garras infernais e atingiu {heroi_ataque}, causando 25 pontos de dano!")
                        if herois[heroi_ataque]["vida"] <= 0:
                            print(f"{heroi_ataque} tombou diante do poder do Rei Demônio!")
                            herois_tombados.append(heroi_ataque)
            else:
                herois[heroi_ataque]["vida"] -= 25
                print(f"O Rei Demônio avançou com suas garras infernais e atingiu {heroi_ataque}, causando 25 pontos de dano!")
                if herois[heroi_ataque]["vida"] > 0:
                    if herois[heroi_ataque]["arma"] in reliquias_lendarias:
                        rei_demonio["vida"] -= reliquias_lendarias[herois[heroi_ataque]["arma"]]
                        print(f"{heroi_ataque} brandiu {herois[heroi_ataque]['arma']} contra o Rei Demônio e causou {reliquias_lendarias[herois[heroi_ataque]['arma']]} pontos de dano!")
                        if rei_demonio["vida"] <= 0:
                            print(f"Com um golpe decisivo, {heroi_ataque} derrota o Rei Demônio! Após uma longa batalha, o Reino Celeste está finalmente livre de sua ameaça!")
                    else:
                        print("A arma do herói não possui poder suficiente para atravessar a aura sombria do Rei Demônio!")
                        if rei_demonio["vida"] > 0:
                            herois[heroi_ataque]["vida"] -= 25
                            print(f"O Rei Demônio avançou com suas garras infernais e atingiu {heroi_ataque}, causando 25 pontos de dano!")
                            if herois[heroi_ataque]["vida"] <= 0:
                                print(f"{heroi_ataque} tombou diante do poder do Rei Demônio!")
                                herois_tombados.append(heroi_ataque)
                else:
                    print(f"{heroi_ataque} tombou diante do poder do Rei Demônio!")
                    herois_tombados.append(heroi_ataque)
           
if herois_suficientes:             
    if len(herois_tombados) == len(herois):
        print("O último herói tombou. Vitorioso, o Rei Demônio retoma sua marcha sombria em direção ao Reino Celeste!")
    elif len(herois_tombados) == 0:
        print("Contra todas as expectativas, todos os heróis retornaram vivos ao Reino Celeste. Naquela noite, nenhuma nova inscrição precisou ser feita no Memorial dos Heróis.")            
    else:
        print("A vitória foi conquistada, mas teve seu preço. Alguns heróis não retornaram do campo de batalha e seus nomes serão eternizados no Memorial dos Heróis.")
    if len(herois_tombados) > 0:
        print("--- Memorial dos Heróis Caídos ---")
        for heroi in herois_tombados:
            print(heroi)
                
