entrada = ""
lista_entrada = []
zona_prioritaria = []
zona_acompanhamento = []

while entrada.upper() != "FIM":
    entrada = input()
    
    if entrada.upper() != "FIM":
        info = entrada.split(",")
        nome = info[0]
        faccao = info[1]
        dano_base = float(info[2])
        inteligencia = int(info[3])
        fator_caos = float(info[4])
        
        nivel_inicial = dano_base + (inteligencia * fator_caos)
        nivel_ameaca = nivel_inicial
        if faccao == "Enclave":
            nivel_ameaca = nivel_inicial - (nivel_inicial * 0.15)
        
        tupla = (-nivel_ameaca, nome, faccao)
        
        lista_entrada.append(tupla)

if len(lista_entrada) > 0:
    nova_lista = lista_entrada[0::]
    lista_faccoes = []
    for i in nova_lista:
        lista_faccoes.append(i[2])
    lista_freq = []
    for i in lista_faccoes:
        if i not in lista_freq:
            lista_freq.append(i)
    
    for i in range(0, len(lista_freq)):
        lista_freq[i] = [lista_freq[i], lista_faccoes.count(lista_freq[i])]      
    

    lista_atualizada = []

    for i in lista_entrada:
        for j in lista_freq:
            if i[2] == j[0]:
                nivel_ajustado = abs(i[0]) + (abs(i[0]) * 0.05 * (j[1] - 1))
                lista_atualizada.append((-nivel_ajustado, i[1], i[2]))

    lista_atualizada.sort()

    zona_prioritaria = lista_atualizada[0:3]
    zona_acompanhamento = lista_atualizada[3::]
   
print(zona_prioritaria)