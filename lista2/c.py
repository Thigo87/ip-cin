paciencia_shrek = int(input())
qtd_visitantes = 0

visitante = ""
gasto_paciencia = 0

print("Shrek achava que morar em um pântano afastado seria suficiente para manter as pessoas longe. Ele estava muito enganado.")

while paciencia_shrek != 0 and gasto_paciencia <= paciencia_shrek and visitante != "ninguém":
    visitante = input()
    if visitante == "Burro":
        gasto_paciencia = int(input())
        print("Burro?! Eu acabei de pedir um pouco de paz!")
        assunto = input()
        if assunto == "sanduíche":
            gasto_paciencia /= 2
            if gasto_paciencia <= paciencia_shrek:
                qtd_visitantes += 1
                print("Ah, isso sim é um bom assunto!") 
        elif assunto == "Fiona":
            if gasto_paciencia <= paciencia_shrek:
                qtd_visitantes += 1
                print("É o Burro! E, como sempre, ele só sabe falar da Fiona.")
        elif assunto == "pântano":
            if gasto_paciencia <= paciencia_shrek:
                qtd_visitantes += 1
                print("Burro, isso é MEU pântano...")
    elif visitante == "Gato de Botas":
        gasto_paciencia = int(input())
        if gasto_paciencia <= paciencia_shrek:
            qtd_visitantes += 1
            print("O Gato de Botas chegou! Shrek já está de olho nas suas botas.")
    elif visitante == "Pinóquio":
        gasto_paciencia = int(input())
        if gasto_paciencia <= paciencia_shrek:
            qtd_visitantes += 1
            print("Pinóquio chegou! Shrek espera que ele não esteja mentindo.")
    elif visitante == "Lobo Mau":
        gasto_paciencia = int(input())
        if gasto_paciencia <= paciencia_shrek:
            qtd_visitantes += 1
            print("Lobo Mau?! Shrek abriu a porta, mas já está se arrependendo!")
    else:
        if visitante != "ninguém":
            gasto_paciencia = int(input())
            if gasto_paciencia <= paciencia_shrek:
                qtd_visitantes += 1
                print("Visitante desconhecido! Shrek não sabe quem você é, mas pode entrar por sua conta em risco.")
    
    paciencia_shrek -= gasto_paciencia

if paciencia_shrek <= 0:
    print("A paciência do Shrek acabou! Dê meia-volta antes que ele perca o controle!")
else:
    print("Ufa! Ninguém apareceu. Finalmente, um pouco de paz no pântano!")

print(f"Ao todo, {qtd_visitantes} visitantes passaram pelo pântano. Shrek sobreviveu a mais um dia!")