vida_noel = 100
dano_breu = 15

presentes = 0
carvao = 0 

streak_p = 0
streak_c = 0

nome_localidade = ""

aviso_sobrecarga = False

custo_total = 0

while vida_noel > 0 and nome_localidade != "FIM":
    nome_localidade = input()
    if nome_localidade != "FIM":
        continente = input()
        pais = input()
        custo_base = 10
        custo_log = 0
        fator_continental = 1.0
        modificador_nacional = 1.0
        
        if continente.lower() == "europa":
            fator_continental = 1.0
        elif continente.lower() == "oceania":
            fator_continental = 2.0
        elif continente.lower() == "américa":
            fator_continental = 3.0
        elif continente.lower() == "áfrica":
            fator_continental = 4.0
        elif continente.lower() == "ásia":
            fator_continental = 5.0
        
        if pais.lower() == "brasil":
            modificador_nacional = 1.10
        elif pais.lower() == "eua":
            modificador_nacional = 1.15
        elif pais.lower() == "china":
            modificador_nacional = 1.20
        elif pais.lower() == "canadá":
            modificador_nacional = 1.25
        elif pais.lower() == "rússia":
            modificador_nacional = 1.30
    
    if nome_localidade != "FIM" and vida_noel > 0:
        nome_crianca_ou_evento = ""
        while nome_crianca_ou_evento != "FIM_LOCAL" and vida_noel > 0:
            nome_crianca_ou_evento = input()
            if custo_log > 100:
                if not aviso_sobrecarga:
                    print("O trenó está sobrecarregado pela magia! Custos base aumentados.")
                    aviso_sobrecarga = True
                custo_base = 15        
            if nome_crianca_ou_evento != "Breu" and nome_crianca_ou_evento != "FIM_LOCAL":
                custo_log += custo_base * fator_continental * modificador_nacional 
                pontuacao = input()
                while int(pontuacao) < 0 or int(pontuacao) > 100:
                    if pontuacao.isnumeric() or "-" in pontuacao:
                        print("Pontuação inválida, insira novamente.")
                    pontuacao = input()
                if int(pontuacao) >= 70:
                    print(f"{nome_crianca_ou_evento} foi uma boa criança este ano e receberá um presente!")
                    presentes += 1
                    streak_p += 1
                    streak_c = 0
                else:
                    print(f"{nome_crianca_ou_evento} não se comportou bem e receberá carvão.")
                    carvao += 1
                    streak_c += 1
                    streak_p = 0
                
                if streak_p == 3:
                    print("A fé das crianças fortalece a magia! Noel recuperou 10 de HP.")
                    if vida_noel + 10 > 100:
                        vida_noel == 100
                    else:
                        vida_noel += 10
                    streak_p = 0
                
                if streak_c == 3:
                    dano_breu += 5
                    streak_c = 0
                    print(f"O medo e a descrença alimentam as sombras... O dano de Breu aumentou para {dano_breu}!")
            else: #emboscada
                if nome_crianca_ou_evento != "FIM_LOCAL":
                    print("Alerta! Breu atacou a entrega!")
                    vida_breu = 50
                    n_acao = 1
                    iniciativa = input() #Noel ou Breu
                    if iniciativa == "Noel":
                        while vida_noel > 0 and vida_breu > 0:
                            acao = input()
                            if n_acao % 2 != 0:
                                vida_breu -= 20
                            else:
                                vida_noel -= dano_breu
                            n_acao += 1
                    else:
                        while vida_noel > 0 and vida_breu > 0:
                            acao = input()
                            if n_acao % 2 != 0:
                                vida_noel -= dano_breu     
                            else:
                                vida_breu -= 20
                            n_acao += 1
                    
                    if vida_breu <= 0 and vida_noel > 0:
                        print("Noel repeliu a emboscada e as entregas continuam!")
            
        if  vida_noel > 0:
            print(f"Localidade {nome_localidade} finalizada. Custo logístico: {custo_log:.2f}")
            custo_total += custo_log                    

if vida_noel > 0:
    print(f"Noite concluída com sucesso! Presentes: {presentes} | Carvão: {carvao}")
    print(f"Custo logístico total: {custo_total:.2f}")
    print(f"HP final do Noel: {vida_noel}")
else:
    print("O HP de Noel chegou a zero! O Breu venceu a batalha... O Natal das crianças foi arruinado.")         