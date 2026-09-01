N = int(input())

nome = ""
trabalhos = ""
index = 0

repetidos = 0

for i in range(0, N):
    index += 1 
    vaga = input()
    nome += f"{vaga}-"

index = 0

print("Parabéns formandos! E agora iniciaremos sua carreira nas indústrias Honex.")

for i in nome:
    if i != "-":
        trabalhos += i
    else:
        trabalhos += "-"

aux = ""
final = ""

for trabalho in trabalhos:
    if trabalho == '-':
        index += 1
        if aux not in final:
            if index != 1:
                final += f" - {aux}"
            else:
                final += f"{aux}"
            aux = ""
        else:
            repetidos += 1
            aux = ""
    else:
        aux += f"{trabalho}"

print(final)
print(f"Quantidade de cargos repetidos: {repetidos}")

opcoes = N - repetidos

if opcoes > repetidos:
    print("Pelo menos Barry tem opções!")
else:
    print("Mais do mesmo. Barry será apenas uma engrenagem na máquina de mel.")