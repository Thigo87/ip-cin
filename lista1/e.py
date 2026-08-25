lugar = input() #recebe o lugar que o Byte irá investigar
pista = input() #recebe a pista encontrada por Byte
suspeito = input() #recebe o suspeito, podendo ser um professor ou pseudoConselheiro
alibi = input() #local que o suspeito diz que estava

kaonelle = False
notaFiscal = False
bone = False
balao = False
passagem = False
professor = False


#primeiro output
print("Um bom faro nunca falha! E o meu tá apontando pra uma covardia: sumiram TODOS os monitores! Eu passo o dia perseguindo o próprio rabo, mas juro que hoje acho eles mais rápido que isso!")

#output de acordo com os lugares
if lugar == "Grad 5":
    print("O laboratório mais movimentado do CIn... e nenhum sinal de monitor por aqui.")
elif lugar == "Kaonelle":
    print("Byte farejou cada mesa da Kaonelle em busca de pistas.")
    kaonelle = True
elif lugar == "DA":
    print("A sala de convivência estava vazia. Até as bolinhas de ping pong sumiram.")
elif lugar == "Feirinha do CIn":
    print("No meio da Feirinha, muita gente, mas nenhum monitor à vista.")

#de acordo com as pistas
if pista == "nota fiscal":
    notaFiscal = True
    if kaonelle:
        print("A nota fiscal é de uma compra de 350 cãoxinhas. Alguém está planejando alimentar um exército — ou uma festa e tanto.")
    else:
        print("Uma nota fiscal misteriosa, mas as informações estão meio apagadas.")
elif pista == "boné":
    bone = True
    print("Um boné caído no chão. Alguém saiu correndo e esqueceu a cabeça descoberta.")
elif pista == "balão":
    balao = True
    print("Um balão murcho no chão... isso aqui cheira a comemoração.")
elif pista == "passagem para Catende":
    passagem = True
    print("Uma passagem de ônibus para Catende. Alguém tem raízes por lá.")

#verificando se o suspeito é professor
if suspeito == "Ricardo Maneiro" or suspeito == "Fernanda Arvore" or suspeito == "Marciano" or suspeito == "Amanda da Arte" or suspeito == "Yoda":
    professor = True

#de acordo com o suspeito
if professor:
    if balao or (kaonelle and notaFiscal):
        print(f"{suspeito} alega o álibi: {alibi}. Diz estar ocupado com os preparativos de algo... mas não entrega do que se trata.")
    else:
        print(f"{suspeito} alega o álibi: {alibi}. Diz só estar corrigindo provas atrasadas. Nada a ver com o caso.")
else:
    if suspeito == "Jaobé":
        if passagem:
            print(f"Diante da pista encontrada, Jaobé gagueja e alega o álibi: {alibi}. A coincidência é grande demais.")
        else:
            print(f"Jaobé alega o álibi: {alibi}. Sem essa pista específica, nada o liga ao caso.")
    elif suspeito == "Jorge Arthur":
        if bone:
            print(f"Jorge Arthur alega o álibi: {alibi}... mas, estranhamente, está sem boné pela primeira vez na vida. Algo não bate.")
        else:
            print(f"Jorge Arthur alega o álibi: {alibi}. Sem essa pista específica, nada o liga ao caso.")
            
#desfecho
if alibi == lugar:
    if professor:
        if balao or (notaFiscal and kaonelle):
            print("CASO ENCERRADO: Não houve crime algum! Os monitores, emocionados com a volta de Byte, prepararam uma festa surpresa, com direito a muita cãoxinha e bolinho de ração pra ele. O banquete foi ótimo... pelo menos pra quem é cachorro.")
        else:
            print("CASO EM ABERTO: Byte se distraiu perseguindo um esquilo no meio do pátio e esqueceu completamente onde tinha parado a investigação. Sem solução dessa vez.")
    elif suspeito == "Jaobé":
        if passagem:
            print("CASO ENCERRADO: Jaobé e Jorge Arthur, enfurecidos por não terem honra o suficiente para serem conselheiros, sequestraram todos os monitores e só os libertariam em troca dos cargos. Byte percebe que o álibi contado bate exatamente com o lugar onde a pista foi encontrada, o flagrante perfeito! Byte morde a canela dos dois e resgata a equipe. Os culpados levam um puxão de orelha e são exilados da monitoria.")
        else:
            print("CASO EM ABERTO: Byte se distraiu perseguindo um esquilo no meio do pátio e esqueceu completamente onde tinha parado a investigação. Sem solução dessa vez.")
    elif suspeito == "Jorge Arthur":
        if bone:
            print("CASO ENCERRADO: Jaobé e Jorge Arthur, enfurecidos por não terem honra o suficiente para serem conselheiros, sequestraram todos os monitores e só os libertariam em troca dos cargos. Byte percebe que o álibi contado bate exatamente com o lugar onde a pista foi encontrada, o flagrante perfeito! Byte morde a canela dos dois e resgata a equipe. Os culpados levam um puxão de orelha e são exilados da monitoria.")
        else:
            print("CASO EM ABERTO: Byte se distraiu perseguindo um esquilo no meio do pátio e esqueceu completamente onde tinha parado a investigação. Sem solução dessa vez.")
else:
    print("CASO EM ABERTO: Byte se distraiu perseguindo um esquilo no meio do pátio e esqueceu completamente onde tinha parado a investigação. Sem solução dessa vez.")