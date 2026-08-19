G = int(input())

print("Nossa, que lindo cavalo! Mas deixe-me verificar apenas uma coisa...")

duplas = G//2

if G != 0:
    print("ARMADILHA")
    if G % 2 == 0:
        print(f"OS GUERREIROS FORMARAM {duplas} DUPLAS")
    else:
        print(f"OS GUERREIROS FORMARAM {duplas} DUPLAS E UM GUERREIRO FICOU SOZINHO")
else:
    print("ENTRADA LIBERADA")