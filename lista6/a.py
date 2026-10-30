def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)
    
def mdc(a, b):
    if a == 0 or b == 0:
        return a if b == 0 else b
    else:
        ordem = [a, b if a >= b else b, a]
        divisao = ordem[0] // ordem[1]
        resto = ordem[0] - (ordem[1]*divisao)
        ordem = [ordem[1], resto]
        return mdc(ordem[0], ordem[1])

def divisor(duendes, elfos, mdc):
    return ((duendes + elfos) // 2) + mdc

def potencia(num, exp):
    if exp == 0:
        return 1
    else:
        return num * potencia(num, exp - 1)
    
def lancamento(producao_1, producao_2):
    return potencia(producao_1, 2) + potencia(producao_2, 2)

valor_duendes = int(input())
valor_elfos = int(input())

fatorial_duendes = fatorial(valor_duendes)
fatorial_elfos = fatorial(valor_elfos)

if fatorial_duendes > fatorial_elfos:
    print("Os duendes se superaram dessa vez.")
elif fatorial_duendes < fatorial_elfos:
    print("É, os elfos tiveram um resultado melhor.")
else:
    print("Ué, houve um empate.")

mdc_valores = mdc(fatorial_duendes, fatorial_elfos)
if mdc_valores > 10:
    print("Caixas gigantes! O Papai Noel vai precisar de um guindaste para empacotar tudo.")
else:
    print("Caixas compactas e organizadas perfeitamente.")
    
estabilidade = divisor(fatorial_duendes, fatorial_elfos, mdc_valores)

if estabilidade > 50:
    print("Atenção: O divisor de estabilidade está altíssimo!")
else:
    print("Divisor calculado com sucesso. A rampa está equilibrada.")
    
print("Calculando a inclinação geométrica do canhão...")

if lancamento(fatorial_duendes, fatorial_elfos) % estabilidade != 0:
    print("Lançamento autorizado!")
else:
    print("Lançamento não autorizado!")