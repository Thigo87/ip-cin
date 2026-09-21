herois = []
cadastro_heroi = ""
while cadastro_heroi.upper() != "FIM":
    cadastro_heroi = input()
    if cadastro_heroi.upper() != "FIM":
        herois.append(cadastro_heroi.split(" - "))

print(herois)