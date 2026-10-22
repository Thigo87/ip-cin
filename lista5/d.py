variacoes = {
    "a": "aáàâãäAÁÀÂÃÄ",
    "e": "eéèêëEÉÈÊË",
    "i": "iíìîïIÍÌÎÏ",
    "o": "oóòôõöOÓÒÔÕÖ",
    "u": "uúùûüUÚÙÛÜ"
}
consoantes = "bcdfghjklmnpqrstvwxyz"
animagos = {}

frase = input()
letra_consulta = input()

for letra in frase:
    if letra in consoantes or letra in consoantes.upper():
        if letra.lower() in animagos:
            if letra in animagos[letra.lower()]:
                animagos[letra.lower()][letra] += 1
            else:
                animagos[letra.lower()].update({letra : 1})
        else:
            animagos.update({letra.lower() : {letra : 1}})
    else:
        letra_real = ""
        for vogal in variacoes:
            if letra in variacoes[vogal]:
                letra_real = vogal
        if letra_real in variacoes:
            if letra_real in animagos:
                if letra in animagos[letra_real]:
                    animagos[letra_real][letra] += 1
                else:
                    animagos[letra_real].update({letra : 1})
            else:
                animagos.update({letra_real : {letra : 1}})

qntd_letras = []

for letra in animagos:
    counter = 0
    for disfarce in animagos[letra]:
        counter += animagos[letra][disfarce]

    qntd_letras.append(f"{counter}{letra}")

for i in range(len(qntd_letras) - 1):
    for j in range(len(qntd_letras) - i - 1):
        num1 = ""
        num2 = ""
        for n in qntd_letras[j]:
            if n.isnumeric():
                num1 += n
        for n in qntd_letras[j + 1]:
            if n.isnumeric():
                num2 += n
        if int(num1) < int(num2):            
            qntd_letras[j], qntd_letras[j + 1] = qntd_letras[j + 1], qntd_letras[j]

frase = ""
for qntd in qntd_letras:
    frase += f"{qntd} "

frase = frase[:len(frase) - 1]

qntd_letra_escolhida = 0
for disfarce in animagos[letra_consulta]:
    qntd_letra_escolhida += animagos[letra_consulta][disfarce]

qntd_variacoes = len(animagos[letra_consulta])

variacao_frequente = ""
qntd_variacao_frequente = 0

for variacao in animagos[letra_consulta]:
    if animagos[letra_consulta][variacao] > qntd_variacao_frequente:
        qntd_variacao_frequente = animagos[letra_consulta][variacao]
        variacao_frequente = variacao

print(frase)
print(f"Total de ocorrências: {qntd_letra_escolhida}")
print(f"Quantidade de variações: {qntd_variacoes}")
print(f"Variação mais frequente: {variacao_frequente} ({qntd_variacao_frequente})")