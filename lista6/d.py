def reversa(palavra, tamanho):
    if tamanho <= 0:
        return palavra[tamanho][:0]
    else:
        tamanho -= 1
        return palavra[tamanho] + reversa(palavra, tamanho)

palavra = ""
pontos = 0
palavras_investigadas = []
validas = 0


print("🎄 Alerta na Vila dos Quem! O Grinch sumiu com os presentes! Vamos investigar as pistas!")

while palavra != "FIM":
    palavra = input().upper()
    if palavra != "FIM":
        print("🔎 Qual será a próxima pista?")
        if palavra in palavras_investigadas:
            print("🚫 Pistas repetidas não vão nos ajudar em nada!")
        else:
            if palavra == "OSSO" and palavra not in palavras_investigadas:
                palavras_investigadas.append(palavra)
                validas += 1
                pontos += 3
                print(f"✅ Parece que a pista '{palavra}' é um palíndromo!")
                print("🐶 O osso do Max! O Grinch esteve por aqui! (+3 pontos)")
            elif palavra == "RADAR" and palavra not in palavras_investigadas:
                palavras_investigadas.append(palavra)
                validas += 1
                pontos += 5
                print(f"✅ Parece que a pista '{palavra}' é um palíndromo!")
                print("🛷 O radar do trenó! Estamos na trilha certa! (+5 pontos)")
            elif palavra == "REVIVER" and palavra not in palavras_investigadas:
                palavras_investigadas.append(palavra)
                validas += 1
                pontos += 10
                print(f"✅ Parece que a pista '{palavra}' é um palíndromo!")
                print("💚 Reviver o Natal... será que o Grinch está se arrependendo? (+10 pontos)")
            elif palavra == "ARARA" and palavra not in palavras_investigadas:
                palavras_investigadas.append(palavra)
                pontos -= 4
                print(f"✅ Parece que a pista '{palavra}' é um palíndromo!")
                print("🦜 Era uma arara de brinquedo! O Grinch plantou uma pista falsa! (-4 pontos)")
            elif palavra == "SOS" and palavra not in palavras_investigadas:
                palavras_investigadas.append(palavra)
                pontos -= 2
                print(f"✅ Parece que a pista '{palavra}' é um palíndromo!")
                print("📻 Era um pedido de socorro falso! O Grinch está nos desviando do caminho! (-2 pontos)")
            elif reversa(palavra, len(palavra)) == palavra: #verificando se é palíndrome
                palavras_investigadas.append(palavra)
                pontos += 1
                validas += 1
                print(f"✅ Parece que a pista '{palavra}' é um palíndromo!")
            else:
                if palavra not in palavras_investigadas:
                    palavras_investigadas.append(palavra)
                    print(f"❌ Poxa! Parece que a pista '{palavra}' não nos ajudou muito...")

print("📁 Parece que a investigação terminou!")
print("")
print("Vamos à Análise Final! 📋")
print("")
print(f"Pistas investigadas: {len(palavras_investigadas)}")
print(f"Palíndromos encontrados: {validas}")
print(f"Aproveitamento: {((validas/len(palavras_investigadas)) * 100 if len(palavras_investigadas) != 0 else 0):.1f}%")
print(f"Pontos de Evidência: {pontos}")
print("")

if len(palavras_investigadas) == 0:
    print("Sem pistas, sem caso! O Grinch está rindo lá do Monte Crumpit... 😈")
elif validas == 0:
    print("Nenhuma pista válida! O Grinch fugiu levando até o último enfeite! 💨")
elif ("OSSO" and "RADAR" and "REVIVER") in palavras_investigadas:
    print("Caso encerrado! O coração do Grinch cresceu três tamanhos e ele devolveu os presentes! 🎅💚")
elif (validas/len(palavras_investigadas)) >= 0.75:
    print("Estamos quase lá! O Grinch já está ouvindo os cantos de Natal da Vila! 🎶")
elif (validas/len(palavras_investigadas)) >= 0.5:
    print("A trilha está esquentando! Mais um pouco e pegamos o Grinch! 🔎")
elif (validas/len(palavras_investigadas)) < 0.5:
    print("Poucas pistas válidas... O Grinch está fazendo piada lá do Monte Crumpit. 🏔️")