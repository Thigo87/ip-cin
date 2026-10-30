def avaliacao_energia(num):
    pass

def avaliacao_brilho(num):
    pass
n = int(input())

print("SISTEMA DE CALIBRAGEM DA ÁRVORE QUÂNTICA DE NATAL\nOficina Central do Papai Noel - Setor de Engenharia Fractal v1.0")
print("")
print("[INFO] Carregando protocolos de recursão dos duendes... [INFO] Conectando ao gerador de auroras boreais...")
print("")
print(f"[PROCESSANDO] Calculando as camadas fractais para o nível {n}...")
print("[AGUARDE] Desdobrando a pilha de recursão no núcleo do cristal...")
print("")

energia_acumulada = avaliacao_energia(n)
print(f"[RELATÓRIO DE ENERGIA ACUMULADA]\nA soma dos índices de energia do nível 0 até o nível {n} é {energia_acumulada:.4f}.")
print("")

fator_brilho = avaliacao_brilho(n)
if fator_brilho == 0:
    print(f"[AVISO DO DUENDE CHEFE]: Você acessou o Núcleo Primordial (Nível 0)!\nEste cristal não possui camadas externas, mas sua pureza de {fator_brilho} é máxima.")
    print("")
elif fator_brilho < 0.35:
    print(f"[STATUS DO CRISTAL]: Fator de Brilho = {fator_brilho}\nResultado: Brilho Fraco! O cristal está absorvendo pouca energia.\nDica do Papai Noel: Tente aumentar o nível da árvore para iluminar o Polo Norte!")
    print("")
elif fator_brilho > 0.42:
    print(f"[STATUS DO CRISTAL]: Fator de Brilho = {fator_brilho}\nResultado: SUPERCARGA ENERGÉTICA DETECTADA!\nCuidado! O cristal está gerando tanto brilho que pode fazer o trenó voar mais rápido do que o permitido!")
    print("")
else:
    print(f"[STATUS DO CRISTAL]: Fator de Brilho = {fator_brilho}\nResultado: RESSONÂNCIA PERFEITA!\nAtenção, duendes! Este cristal está pronto para ir direto para o topo de nossa Árvore de Natal!")
    print("")
    
print("Calibração encerrada com sucesso!\nQue o seu código compile na primeira tentativa. Feliz Natal!")