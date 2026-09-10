ano_origem = int(input())
ano_proibido = int(input())
energia = int(input())

ano_atual = ano_origem
pecas = 0
salto = 0
pecas = 0
rasgo_temporal = 0

missao_cumprida = False
falha = False

final = ""

print("=== WABAC: SISTEMA DE EMERGÊNCIA ===\nAlvo: Ano 2026 | Peças Necessárias: 3\nSherman, mantenha as mãos longe dos botões! Iniciando saltos...")

while missao_cumprida == False and falha == False:
    if energia <= 0:
        energia = 0
        falha = True
        final = "apagao"
    if rasgo_temporal >= 100:
        rasgo_temporal = 100
        falha = True
        final = "rasgo"
    if missao_cumprida == False and falha == False: 
        acao = input()
        if acao == "SALTAR":
            salto += 1
            anos_salto = int(input())
            custo_energia = int(input())
            rasgo_temporal += 10
            ano_atual += anos_salto
            energia -= custo_energia
            if ano_atual == ano_origem or ano_atual == ano_proibido:
                falha = True
                final = "duplicata"
            if ano_atual >= 2026 and pecas >= 3:
                    missao_cumprida = True
            
            if not falha and energia > 0 and not missao_cumprida:
                print(f"WABAC saltou para o ano {ano_atual}!\nEnergia restante: {energia} | Rasgo Temporal: {rasgo_temporal}%")
            
        elif acao == "CONSERTAR":
            dificuldade = int(input())
            esforco_sherman = int(input())
            if esforco_sherman >= dificuldade:
                pecas += 1
                energia -= 10
                print('Sherman: "Consegui, Mr. Peabody! Encontrei uma peça de calibragem!"')
                print(f"Peças coletadas: {pecas}/3 | Energia: {energia}")
                if pecas >= 3 and ano_atual >= 2026:
                    missao_cumprida = True
            else:
                energia -= 15
                rasgo_temporal += 20
                if rasgo_temporal < 100:
                    print('Mr. Peabody: "Tenha mais cuidado, Sherman! Essa falha desestabilizou o tempo!"')
                    print(f"Energia: {energia} | Rasgo Temporal: {rasgo_temporal}%")
        elif acao == "AULA DE HISTÓRIA":
            energia += 25
            rasgo_temporal += 15
            print('Mr. Peabody: "Como disse Galileu Galilei, a matemática é a linguagem com a qual Deus escreveu o universo."')
            print(f"Energia recarregada para {energia}!")
        elif acao == "ABORTAR":
            falha = True
            final = "aborto"
            
        
if falha:
    if final == "duplicata":
        print(f"ALERTA CRÍTICO: Peabody encontrou sua própria versão no ano {ano_atual}!\nO continuum espaço-tempo ruiu em uma espiral paradoxal.")
    elif final == "apagao":
        print("A WABAC desligou completamente por falta de energia.\nPeabody e Sherman estão vagando sem rumo pela linha do tempo...")
    elif final == "rasgo":
        print("O rasgo temporal atingiu massa crítica!\nO universo foi engolido por um buraco negro sobre a cidade de Nova York.")
    elif final == "aborto":
        print("Mr. Peabody acionou o protocolo de parada manual.\nA viagem foi cancelada antes de sua conclusão.")
            
else:
    print(f"A WABAC emergiu com sucesso no ano de {ano_atual}! Com as 3 peças coletadas, Mr. Peabody selou o rasgo temporal e salvou o presente!")