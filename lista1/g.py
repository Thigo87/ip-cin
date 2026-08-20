visita1 = input()
veredito1 = input()

visita2 = input()
veredito2 = input()

visitasValidas = 0
gostou = 0
naoGostou = 0

zonaSul = 0

print("Depois que a Série A e a Libertadores ficaram só no sonho do Santa, Byte pendura a chuteira de ídolo tricolor e parte pro interior: começa a Excursão Interiorana em busca do time da sua vida!")

if "Catende" in visita1:
    print("Catende!!! Aqui já rodou a maior usina de açúcar e álcool da América Latina, Byte sente o orgulho no ar.")
    zonaSul += 1
elif "Palmares" in visita1:
    print("Palmares, a Terra dos Poetas! Berço de nomes como Ascenso Ferreira, aqui até o futebol merece um verso.")
    zonaSul += 1
elif "Carcará" in visita1:
    print("Carcará no peito! Essa é terra de Salgueiro, o primeiro clube do interior a ser campeão pernambucano, Byte sente o chamado do Sertão!")
    visitasValidas += 1
elif "Patativa" in visita1:
    print("Show da Patativa! Caruaru e o Central esperam Byte de braços abertos, direto da maior feira a céu aberto do mundo!")
    visitasValidas += 1
elif "Azulão" in visita1:
    print("Ar puro de serra! O Azulão de Bonito, sensação recente do Pernambucano, pode ser o novo lar de Byte!")
    visitasValidas += 1
elif "fruticultura" in visita1:
    print("Margens do Velho Chico! Petrolina, a maior cidade do interior, com direito a manga, uva e muita irrigação, chama Byte pro time!")
    visitasValidas += 1
elif "Pássaro Preto" in visita1:
    print("Pertinho de casa! O Pássaro Preto, orgulhosamente um dos times mais folclóricos do planeta, também está de olho em Byte!")
    visitasValidas += 1
if veredito1 == "GOSTOU":
    print("Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.")
    gostou += 1
elif veredito1 == "NÃO GOSTOU":
    print("Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.")
    naoGostou += 1
    
if "Catende" in visita2:
    print("Catende!!! Aqui já rodou a maior usina de açúcar e álcool da América Latina, Byte sente o orgulho no ar.")
    zonaSul += 1
elif "Palmares" in visita2:
    print("Palmares, a Terra dos Poetas! Berço de nomes como Ascenso Ferreira, aqui até o futebol merece um verso.")
    zonaSul += 1
elif "Carcará" in visita2:
    print("Carcará no peito! Essa é terra de Salgueiro, o primeiro clube do interior a ser campeão pernambucano, Byte sente o chamado do Sertão!")
    visitasValidas += 1
elif "Patativa" in visita2:
    print("Show da Patativa! Caruaru e o Central esperam Byte de braços abertos, direto da maior feira a céu aberto do mundo!")
    visitasValidas += 1
elif "Azulão" in visita2:
    print("Ar puro de serra! O Azulão de Bonito, sensação recente do Pernambucano, pode ser o novo lar de Byte!")
    visitasValidas += 1
elif "fruticultura" in visita2:
    print("Margens do Velho Chico! Petrolina, a maior cidade do interior, com direito a manga, uva e muita irrigação, chama Byte pro time!")
    visitasValidas += 1
elif "Pássaro Preto" in visita2:
    print("Pertinho de casa! O Pássaro Preto, orgulhosamente um dos times mais folclóricos do planeta, também está de olho em Byte!")
    visitasValidas += 1
if veredito2 == "GOSTOU":
    print("Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.")
    gostou += 1
elif veredito2 == "NÃO GOSTOU":
    print("Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.")
    naoGostou += 1
    
if zonaSul == 2:
    print("Catende e Palmares na excursão? Aí sim Byte tá garimpando ouro puro da Zona da Mata Sul! Pena que acabou por aqui.")

print("")
print(f"RELATÓRIO DA EXCURSÃO SERTANEJA DO BYTE:\n- Visitas que contaram: {visitasValidas}\n- Gostou: {gostou}\n- Não gostou: {naoGostou}")
print("")
print("E assim termina a Excursão Interiorana de Byte em Pernambuco. Anotar tudo isso na unha, sem laço nem lista, dá um trabalhão! Nas próximas férias, Byte espera que a molecada já saiba de laços, listas e funções pra dar conta do recado com estilo :)")