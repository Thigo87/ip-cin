preparo = 0

energia = int(input())

if energia >= 70:
    preparo += 2
elif energia < 30:
    preparo -= 2

petisco = int(input())
agua = int(input())

if petisco >= 2 and agua >= 1:
    preparo += 2
    
bateria_coleira = int(input())
gps = input()

if bateria_coleira >= 50 and gps == "sim":
    preparo += 2
elif bateria_coleira <= 20:
    preparo -= 1

bolinha = input()

if bolinha == "sim" or petisco >= 4:
    preparo += 1

chuva = input()
temperatura = int(input())

if chuva == "sim" or temperatura > 32:
    preparo -= 2

sinal = int(input())

if sinal >= 70:
    preparo += 1

print("Byte recebeu um novo chamado! Preparando-se para a aventura...")

if energia >= 70:
    print("Byte está cheio de energia!")
elif energia < 30:
    print("Byte está muito cansado... A missão ficou mais difícil.")

if petisco >= 2 and agua >= 1:
    print("Suprimentos preparados!")

if bateria_coleira >= 50 and gps == "sim":
    print("Coleira tecnológica preparada!")
elif bateria_coleira <= 20:
    print("A bateria da coleira está crítica! Isso pode atrapalhar a missão.")

if bolinha == "sim" or petisco >= 4:
    print("Byte está ainda mais animado para a aventura!")

if chuva == "sim" or temperatura > 32:
    print("O clima não está ajudando... Isso vai dificultar a missão.")

if sinal >= 70:
    print("O sinal está forte! Há algo estranho por perto...")

print("")
print(f"Nível de preparo: {preparo}")

if preparo >= 5:
    print("Byte está pronto! A nova aventura começa agora!")
else:
    print("Byte ainda não está pronto. Melhor se preparar um pouco mais!")