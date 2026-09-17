print("Espaço: a fronteira final. Estas são as viagens da nave estelar Enterprise…")
print("Sua missão de cinco anos: explorar novos mundos, procurar novas vidas e novas civilizações, audaciosamente indo aonde nenhum homem jamais esteve.")
print("Dr. McCoy: Eu sou um médico, não um matemático. Mas tenho que fazer o que precisa ser feito.\n=====")

tamanho_amostra = int(input())
while tamanho_amostra < 5 or tamanho_amostra > 12:
    print("Dr. McCoy: Esse número não é ideal, é possível trazer uma amostra de 5 a 12 indivíduos?")
    tamanho_amostra = int(input())

print(f"Dr. McCoy: Certo, {tamanho_amostra} indivíduos. É um número bom.\n=====")

temperaturas = []
bpm = []
irpm = []
pressao = []

for i in range(0, tamanho_amostra):
    sinal_vital = input()
    contador = 0
    for i in sinal_vital.split("-"):
        termo = list(i.split(" "))
        if len(termo[0]) > 0:
            contador += 1
            temperaturas.append(round(float(termo[0]), 1))
        else:
            contador += 1
            if contador == 2:
                bpm.append(round(float(termo[1]), 1))
            elif contador == 3:
                irpm.append(round(float(termo[1]), 1))
            elif contador == 4:
                pressao.append(round(float(termo[1]), 1))

temperaturas.sort()
bpm.sort()
irpm.sort()
pressao.sort()

print("Relatório de dados da amostra:")
print(f"Temperatura: {temperaturas}")
med_temp = 0
if tamanho_amostra % 2 == 0:
    med_temp = round((temperaturas[int((tamanho_amostra)/2)] + temperaturas[int(((tamanho_amostra)/2) - 1)]) / 2, 1)
    print(f"Mediana: {med_temp}")
else:
    med_temp = round(temperaturas[int((tamanho_amostra - 1)/2)], 1)
    print(f"Mediana: {med_temp}")

print(f"Frequência de pulso fluido: {bpm}")
med_pulso = 0
if tamanho_amostra % 2 == 0:
    med_pulso = round((bpm[int((tamanho_amostra)/2)] + bpm[int(((tamanho_amostra)/2) - 1)]) / 2, 1)
    print(f"Mediana: {med_pulso}")
else:
    med_pulso = round(bpm[int((tamanho_amostra - 1)/2)], 1)
    print(f"Mediana: {med_pulso}")
    
print(f"Frequência de troca gasosa: {irpm}")
med_troca = 0
if tamanho_amostra % 2 == 0:
    med_troca = round((irpm[int((tamanho_amostra)/2)] + irpm[int(((tamanho_amostra)/2) - 1)]) / 2, 1)
    print(f"Mediana: {med_troca}")
else:
    med_troca = round(irpm[int((tamanho_amostra - 1)/2)], 1)
    print(f"Mediana: {med_troca}")
    
print(f"Pressão interna de homeostase: {pressao}")
med_pressao = 0
if tamanho_amostra % 2 == 0:
    med_pressao = round((pressao[int((tamanho_amostra)/2)] + pressao[int(((tamanho_amostra)/2) - 1)]) / 2, 1)
    print(f"Mediana: {med_pressao}")
else:
    med_pressao = round(pressao[int((tamanho_amostra - 1)/2)], 1)
    print(f"Mediana: {med_pressao}")

print("=====")
print("Dr. McCoy: Agora irei medir os sinais do paciente.")
print("=====")

sinais_paciente = input()
sinais_paciente = sinais_paciente.split("-")
temperatura_paciente = round(float(sinais_paciente[0].split(" ")[0]), 1)
bpm_paciente = round(float(sinais_paciente[1].split(" ")[1]), 1)
irpm_paciente = round(float(sinais_paciente[2].split(" ")[1]), 1)
pressao_paciente = round(float(sinais_paciente[3].split(" ")[1]), 1)

print("Relatório final:")
print(f"Temperatura do paciente: {temperatura_paciente}")
print(f"Diferença para a mediana: {round(temperatura_paciente - med_temp, 1)}")
print(f"Frequência de pulso fluido do paciente: {bpm_paciente}")
print(f"Diferença para a mediana: {round(bpm_paciente - med_pulso, 1)}")
print(f"Frequência de troca gasosa: {irpm_paciente}")
print(f"Diferença para a mediana: {round(irpm_paciente - med_troca, 1)}")
print(f"Pressão interna de homeostase: {pressao_paciente}")
print(f"Diferença para a mediana: {round(pressao_paciente - med_pressao, 1)}")

criticos = 0

temp_max = max(temperaturas)
temp_min = min(temperaturas)

if temperatura_paciente < temp_min or temperatura_paciente > temp_max:
    criticos += 1

bpm_max = max(bpm)
bpm_min = min(bpm)

if bpm_paciente < bpm_min or bpm_paciente > bpm_max:
    criticos += 1

irpm_max = max(irpm)
irpm_min = min(irpm)

if irpm_paciente < irpm_min or irpm_paciente > irpm_max:
    criticos += 1

pressao_max = max(pressao)
pressao_min = min(pressao)

if pressao_paciente < pressao_min or pressao_paciente > pressao_max:
    criticos += 1
    
print(f"Quantidade de sinais críticos encontrados: {criticos}")

avaliacao = ""

if criticos >= 2:
    avaliacao = "Alerta Crítico"
else:
    avaliacao = "Estável"
    
print(f"Avaliação final: {avaliacao}")
print("=====")
print("Dr. McCoy: Certo, agora sei o que fazer.")