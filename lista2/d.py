rodadas = int(input())
recorde = int(input())

bolinhosComidos = 0
bolinhosNaRodada = 0
bateuRecordeRodada = False

print("Tigresa: Duvido você bater o recorde, Po!\nPo: Prepare-se para ver o Dragão Guerreiro em ação!")

for rodada in range(0, rodadas):
    if bolinhosComidos < recorde:
        bolinhosNaRodada = 0
        bandejas = int(input())
        for bandeja in range(0, bandejas):
            if bolinhosComidos <= recorde:
                bolinhos = int(input())
                bolinhosComidos += bolinhos
                bolinhosNaRodada += bolinhos
            else:
                bateuRecordeRodada = True
                print("\nTigresa: Mas como?!\nPo: UHUL! CONHEÇA A FORÇA DO DRAGÂO GUERREIRO!!")
                print(f"Rodada {rodada + 1}: Po comeu {bolinhosNaRodada} bolinhos.")
                print(f"\nPo: Ei! Eu ainda não terminei!\nTigresa: Acho que não vou mais subestimar sua fome.\nQue loucura! Po venceu a aposta comendo um total de {bolinhosNaRodada} bolinhos em uma só rodada!")
                    
        if not bateuRecordeRodada:
            if bolinhosNaRodada >= recorde:
                bateuRecordeRodada = True
                print("\nTigresa: Mas como?!\nPo: UHUL! CONHEÇA A FORÇA DO DRAGÂO GUERREIRO!!")
                print(f"Rodada {rodada + 1}: Po comeu {bolinhosNaRodada} bolinhos.")
                print(f"\nPo: Ei! Eu ainda não terminei!\nTigresa: Acho que não vou mais subestimar sua fome.\nQue loucura! Po venceu a aposta comendo um total de {bolinhosNaRodada} bolinhos em uma só rodada!")
                                 
            else:
                if bolinhosNaRodada >= 10:
                    print("\nPo: Delícia! Mais uma rodada finalizada!")
                else:
                    print("\nPo: Ainda tenho espaço para mais!")
                    
                print(f"Rodada {rodada + 1}: Po comeu {bolinhosNaRodada} bolinhos.")
        
if not bateuRecordeRodada: 
    if bolinhosComidos > recorde:
        print(f"\nPo: Eu sabia que conseguiria! O recorde e meu!\nTigresa: Inacreditável... Você realmente venceu a aposta.\nPo venceu a aposta! Ele comeu um total de {bolinhosComidos} bolinhos e superou o recorde de {recorde}!")
    elif bolinhosComidos == recorde:
        print(f"\nPo: Empatamos! Cheguei exatamente no recorde!\nTigresa: Impressionante, mas empatar não basta para vencer a aposta. Venha lavar a louça!\nHouve um empate! Po comeu exatamente {bolinhosComidos} bolinhos e igualou o recorde de {recorde}.")
    else:
        print(f"\nTigresa: Eu avisei, Po! A louça do palácio te espera.\nPo: Ah não... Minhas mãos vão ficar enrugadas...\nTigresa venceu a aposta! Po comeu apenas {bolinhosComidos} bolinhos e não alcançou o recorde de {recorde}.")