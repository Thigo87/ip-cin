rodadas = int(input())
recorde = int(input())

comeu = 0

comeuNaRodada = 0

bateuRecorde = False
bateuRecordeRodada = False

print("Tigresa: Duvido você bater o recorde, Po!\nPo: Prepare-se para ver o Dragão Guerreiro em ação!")

for rodada in range(0, rodadas):
    if bateuRecorde == False and bateuRecordeRodada == False:
        if comeu < recorde:
            bandejas = int(input())
            for bandeja in range(0, bandejas):
                if bateuRecorde == False and bateuRecordeRodada == False:
                    if comeu < recorde:
                        bolinhos = int(input())
                        comeu += bolinhos
                    else:
                        bateuRecordeRodada = True
                        print("\nTigresa: Mas como?!\nPo: UHUL! CONHEÇA A FORÇA DO DRAGÂO GUERREIRO!!")
                        print(f"\nPo: Ei! Eu ainda não terminei!\nTigresa: Acho que não vou mais subestimar sua fome.\nQue loucura! Po venceu a aposta comendo um total de {comeuNaRodada} bolinhos em uma só rodada!")
            comeuNaRodada = abs(comeu - comeuNaRodada)
            if comeuNaRodada >= 10:
                print("\nPo: Delícia! Mais uma rodada finalizada!")
            else:
                print("\nPo: Ainda tenho espaço para mais!")
            print(f"Rodada {rodada + 1}: Po comeu {comeuNaRodada} bolinhos.")
            
        else:
            bateuRecorde = True
            
            

if comeu > recorde:
    print(f"\nPo: Eu sabia que conseguiria! O recorde e meu!\nTigresa: Inacreditável... Você realmente venceu a aposta.\nPo venceu a aposta! Ele comeu um total de {comeu} bolinhos e superou o recorde de {recorde}!")   
elif comeu == recorde:   
    print(f"\nPo: Empatamos! Cheguei exatamente no recorde!\nTigresa: Impressionante, mas empatar não basta para vencer a aposta. Venha lavar a louça!\nHouve um empate! Po comeu exatamente {comeu} bolinhos e igualou o recorde de {recorde}.")         
else:
    print(f"Tigresa: Eu avisei, Po! A louça do palácio te espera.\nPo: Ah não... Minhas mãos vão ficar enrugadas...\nTigresa venceu a aposta! Po comeu apenas {comeu} bolinhos e não alcançou o recorde de {recorde}.")
