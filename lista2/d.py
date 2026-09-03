rodadas = int(input())
recorde = int(input())

bolinhos = 0

print("Tigresa: Duvido você bater o recorde, Po!\nPo: Prepare-se para ver o Dragão Guerreiro em ação!")
total = 0
for i in range(0, recorde):
    if bolinhos < recorde:
        bandejas = int(input())
        for i in range(0, bandejas):
            bolinhos = int(input())
            total += bolinhos
        if bolinhos >= 10:
            print("\nPo: Delícia! Mais uma rodada finalizada!")
        else:
            print("\nPo: Ainda tenho espaço para mais!")
        print(f"Rodada {i}: Po comeu {total} bolinhos.")
    