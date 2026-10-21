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

disfarce_padrao = {"variacao" : 0}

for caractere in frase:#pegando a frase do usuario e vendo cada letra dela

    if caractere.isupper():
        if caractere.lower() in consoantes:
            if animagos.get(caractere.lower(), False):
                animagos[caractere.lower()] += 1
            else:
                animagos.update({caractere.lower():1})

        else:
            for item in variacoes:
                if caractere in variacoes[item]:
                    if animagos.get(caractere, False):
                        animagos[caractere] += 1
                    else:
                        animagos.update({caractere:1})

    else:
        if caractere in consoantes:
            if animagos.get(caractere, False):
                animagos[caractere] += 1
            else:
                animagos.update({caractere:1})

        else:
            for item in variacoes:
                if caractere in variacoes[item]:
                    if animagos.get(caractere, False):
                        animagos[caractere] += 1
                    else:
                        animagos.update({caractere:1})
    lista_remocao = []
    for item in animagos:
        if animagos[item] == 0:
            lista_remocao.append(item)
    for item in lista_remocao:
        del animagos[item]

print(animagos)
        
