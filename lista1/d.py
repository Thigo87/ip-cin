chuva = input()
temperatura = int(input())
energia = int(input())

if chuva == "S":
    if energia > 3:
        print("Brincar de bolinha no laboratório")
    else:
        print("Soneca na caminha do CIn")
else:
    if temperatura > 30:
        if energia == 4 or energia == 5:
            print("Nadar no lago da UFPE")
        else:
            print("Descansar na sombra da árvore")
    elif 14 < temperatura <= 30:
        if energia > 2:
            print("Longo passeio no parque")
        else:
            print("Passeio curto no quarteirão")
    else:
        print("Passeio com roupinha de frio")