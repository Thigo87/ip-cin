def avaliacao_energia(num):
    if num == 0:
        return ((1, 1), 1)
    elif num == 1:
        return ((1, 3), (1/3) + 1)
    else:
        n = avaliacao_energia(num - 1)[0][1]
        d = (2 * avaliacao_energia(num - 1)[0][1]) + avaliacao_energia(num - 2)[0][1]
        return ((n, d), (n/d) + avaliacao_energia(num - 1)[1])
    
n = int(input())

print("SISTEMA DE CALIBRAGEM DA ÁRVORE QUÂNTICA DE NATAL\nOficina Central do Papai Noel - Setor de Engenharia Fractal v1.0")
print("")
print("[INFO] Carregando protocolos de recursão dos duendes...\n[INFO] Conectando ao gerador de auroras boreais...")
print("")
print(f"[PROCESSANDO] Calculando as camadas fractais para o nível {n}...")
print("[AGUARDE] Desdobrando a pilha de recursão no núcleo do cristal...")
print("")

energia_acumulada = avaliacao_energia(n)
calculo_energia = energia_acumulada[0][0]/energia_acumulada[0][1]
fator_brilho = avaliacao_energia(n)[1]
print(f"[RELATÓRIO DE ENERGIA ACUMULADA]\nA soma dos índices de energia do nível 0 até o nível {n} é {fator_brilho:.4f}.")
print("")


if n == 0:
    print(f"[AVISO DO DUENDE CHEFE]: Você acessou o Núcleo Primordial (Nível 0)!\nEste cristal não possui camadas externas, mas sua pureza de {calculo_energia:.4f} é máxima.")
    print("")
elif calculo_energia < 0.35:
    print(f"[STATUS DO CRISTAL]: Fator de Brilho = {calculo_energia:.4f}\nResultado: Brilho Fraco! O cristal está absorvendo pouca energia.\nDica do Papai Noel: Tente aumentar o nível da árvore para iluminar o Polo Norte!")
    print("")
elif calculo_energia > 0.42:
    print(f"[STATUS DO CRISTAL]: Fator de Brilho = {calculo_energia:.4f}\nResultado: SUPERCARGA ENERGÉTICA DETECTADA!\nCuidado! O cristal está gerando tanto brilho que pode fazer o trenó voar mais rápido do que o permitido!")
    print("")
else:
    print(f"[STATUS DO CRISTAL]: Fator de Brilho = {calculo_energia:.4f}\nResultado: RESSONÂNCIA PERFEITA!\nAtenção, duendes! Este cristal está pronto para ir direto para o topo de nossa Árvore de Natal!")
    print("")
    
print("Calibração encerrada com sucesso!\nQue o seu código compile na primeira tentativa. Feliz Natal!")