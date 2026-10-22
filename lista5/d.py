variacoes = {
    "a": "aáàâãäAÁÀÂÃÄ",
    "e": "eéèêëEÉÈÊË",
    "i": "iíìîïIÍÌÎÏ",
    "o": "oóòôõöOÓÒÔÕÖ",
    "u": "uúùûüUÚÙÛÜ"
}
consoantes = "bcdfghjklmnpqrstvwxyz"
animagos = {}
disfarces = {}

frase = input()
letra_consulta = input()

for caractere in frase:#pegando a frase do usuario e vendo cada letra dela

    if caractere.isupper():
        if caractere.lower() in consoantes:
            if animagos.get(caractere.lower(), False):
                animagos[caractere.lower()] += 1
            else:
                animagos.update({caractere.lower():1})
            
            if disfarces.get(caractere, False):
                disfarces[caractere.lower()[caractere]] += 1
            else:
                disfarces.update({caractere.lower():{caractere : 1}})

        else:
            for item in variacoes:
                if caractere in variacoes[item]:
                    if animagos.get(caractere, False):
                        animagos[caractere] += 1
                    else:
                        animagos.update({caractere:1})
                    
                    if disfarces.get(item, False):
                        disfarces[caractere.lower()[caractere]] += 1
                    else:
                        disfarces.update({caractere.lower():{caractere : 1}})

    else:
        if caractere in consoantes:
            if animagos.get(caractere, False):
                animagos[caractere] += 1
            else:
                animagos.update({caractere:1})
                
            if disfarces.get(caractere.lower(), False):
                print(disfarces[caractere.lower()][caractere])
                
            else:
                disfarces.update({caractere.lower():{caractere : 1}})

        else:
            for item in variacoes:
                if caractere in variacoes[item]:
                    if animagos.get(caractere, False):
                        animagos[caractere] += 1
                    else:
                        animagos.update({caractere:1})
                        
                    if disfarces.get(item, False):
                        print(disfarces[caractere])
                    else:
                        disfarces.update({caractere.lower():{caractere : 1}})
    lista_remocao = []
    for item in animagos:
        if animagos[item] == 0:
            lista_remocao.append(item)
    for item in lista_remocao:
        del animagos[item]

print(disfarces)

letras = []
for letra in animagos:
    letras.append(f"{animagos[letra]}{letra}")

for i in range(len(letras) - 1):
    for j in range(len(letras) - i - 1):
        if letras[j][0] < letras[j + 1][0]:
            letras[j], letras[j + 1] = letras[j + 1], letras[j]

frase = ""
for letra in letras:
    frase += f"{letra} "

print(frase)

total = 0
for i in letras:
    if letra_consulta in i:
        total = int(i[0])

print(f"Total de ocorrências: {total}")        
