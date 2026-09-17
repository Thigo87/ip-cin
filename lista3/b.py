kit  = ["taco_beisebol","besta","kit_medico", "feijao_enlatado", "walkie_talkie", "garrafa_agua","biscoito"]
kit_rick = ["colt_357", "distintivo", "radio_comunicador", "cantil", "curativo"]
kit_michonne = ["katana", "amolador", "binoculo", "faixa_curativo", "mapa"]
kit_daryl = ["arco e flecha","flechas","faca_de_caca", "corda", "carne_seca"]
kit_carol = ["facao", "bomba_de_fumaca", "sangue_zumbi", "fosforos", "biscoito"]

sobrevivente = input()

if sobrevivente.lower() == "rick":
    print("Um grande líder sempre ajuda sua equipe, Rick lhe dá uma lanterna para a noite")
    kit.append("lanterna")
    kit.remove("taco_beisebol")
    kit_rick.append("taco_beisebol")
    print(f"Kit atual sobrevivente: {kit}")
    
    for i in range(len(kit)):
        if i >= 2:
            kit_rick.append(kit[i])
    
    l = [kit[0], kit[1]]
    kit = l
    
    print("Agora com as costas mais leves, podemos continuar com a nossa caminhada\n")
    print("Finalmente chegamos em Alexandria!\n")
    print(f"Ufa, podemos ficar aqui por um tempo,{sobrevivente}")
    print("")
    print(f"Kit do sobrevivente: {kit}\n\nKit do {sobrevivente}: {kit_rick}")

elif sobrevivente.lower() == "michonne":
    print("Michonne é uma ótima combatente, ela te dá uma arma para você não passar apertos.")
    kit.append("faca_afiada")
    kit.remove("kit_medico")
    print("Você usou o kit médico para socorrer Michonne!")
    print(f"Kit atual sobrevivente: {kit}")
    for i in range(len(kit)):
        if i >= 2:
            kit_michonne.append(kit[i])
        
    l = [kit[0], kit[1]]
    kit = l
        
    print("Agora com as costas mais leves, podemos continuar com a nossa caminhada\n")
    print("Finalmente chegamos em Alexandria!\n")
    print(f"Ufa, podemos ficar aqui por um tempo,{sobrevivente}")
    print("")
    print(f"Kit do sobrevivente: {kit}\n\nKit do {sobrevivente}: {kit_michonne}")

elif sobrevivente.lower() == "daryl":
    print("Daryl é um ótimo caçador. Ele te dá carne para comer na refeição")
    kit.append("carne")
    aux = kit[1]
    kit[1] = kit_daryl[0]
    kit_daryl[0] = aux

    print(f"Kit atual sobrevivente: {kit}")
    print(f"Kit atual Daryl: {kit_daryl}")
    
    for i in range(len(kit)):
        if i >= 2:
            kit_daryl.append(kit[i])
        
    l = [kit[0], kit[1]]
    kit = l
    
        
    print("Agora com as costas mais leves, podemos continuar com a nossa caminhada\n")
    print("Finalmente chegamos em Alexandria!\n")
    print(f"Ufa, podemos ficar aqui por um tempo,{sobrevivente}")
    print("")
    print(f"Kit do sobrevivente: {kit}\n\nKit do {sobrevivente}: {kit_daryl}")
    
elif sobrevivente.lower() == "carol":
    print("Carol sabe como se esconder dos zumbis. Ela te dá uma ajuda.")
    kit.append("roupa_de_camuflagem")
    
    for i in range(1, 4):
        kit_carol.append(kit[i + 1])
    
    kit_carol.remove("bomba_de_fumaca")
    kit_carol.remove("sangue_zumbi")
    kit_carol.remove("fosforos")
    
    kit.remove(kit[2])
    kit.remove(kit[2])
    kit.remove(kit[2])
    
    for i in range(len(kit)):
        if i >= 2:
            kit_carol.append(kit[i])
        
    l = [kit[0], kit[1]]
    kit = l
        
    print("Agora com as costas mais leves, podemos continuar com a nossa caminhada\n")
    print("Finalmente chegamos em Alexandria!\n")
    print(f"Ufa, podemos ficar aqui por um tempo,{sobrevivente}")
    print("")
    print(f"Kit do sobrevivente: {kit}\n\nKit do {sobrevivente}: {kit_carol}")