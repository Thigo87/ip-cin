rodadas = int(input())
recorde = int(input())

totalBolinhos = 0
bateuRecorde = False
recordeNaRodada = False
totalNaRodada = 0

print("Tigresa: Duvido você bater o recorde, Po!\nPo: Prepare-se para ver o Dragão Guerreiro em ação!")

for i in range(0, rodadas): #início da rodada
    if totalBolinhos >= recorde: #verificação inicial do recorde
        bateuRecorde = True
    else:
        totalNaRodada = 0
        bandejas = int(input())
        for a in range(0, bandejas): #início da bandeja i
            if not bateuRecorde: #verificação se ele já bateu o recorde
                bolinhos = int(input())
                if bolinhos >= recorde: #se ele bateu o recorde na rodada, vem pra esse if
                    recordeNaRodada = True
                    print("\nTigresa: Mas como?!\nPo: UHUL! CONHEÇA A FORÇA DO DRAGÂO GUERREIRO!!")
                else: #se não bateu o recorde, vem para esse else
                    totalBolinhos += bolinhos
                    totalNaRodada += bolinhos
        if totalNaRodada >= 10 and bateuRecorde == False:
            print("\nPo: Delícia! Mais uma rodada finalizada!")
        elif totalNaRodada < 10 and bateuRecorde == False:
            print("\nPo: Ainda tenho espaço para mais!")          
        print(f"Rodada {i + 1}: Po comeu {totalNaRodada} bolinhos.")

if bateuRecorde:
    print("\nPo: Eu sabia que conseguiria! O recorde e meu!")
    print("Tigresa: Inacreditável... Você realmente venceu a aposta.")
    print(f"Po venceu a aposta! Ele comeu um total de {totalBolinhos} bolinhos e superou o recorde de {recorde}!")
else:
    if totalBolinhos == recorde:
        print("\nPo: Empatamos! Cheguei exatamente no recorde!")
        print("Tigresa: Impressionante, mas empatar não basta para vencer a aposta. Venha lavar a louça!")
        print(f"Houve um empate! Po comeu exatamente {totalBolinhos} bolinhos e igualou o recorde de {recorde}.")
    if recordeNaRodada:
        print("\nPo: Ei! Eu ainda não terminei!")
        print("Tigresa: Acho que não vou mais subestimar sua fome.")
        print(f"Que loucura! Po venceu a aposta comendo um total de {totalNaRodada} bolinhos em uma só rodada!")
    else:
        print("\nTigresa: Eu avisei, Po! A louça do palácio te espera.")
        print("Po: Ah não... Minhas mãos vão ficar enrugadas...")
        print(f"Tigresa venceu a aposta! Po comeu apenas {totalBolinhos} bolinhos e não alcançou o recorde de {recorde}.")