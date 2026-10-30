def combinacao(a, b):
    if b == 0 or a == b:
        return 1
    else:
        return combinacao(a-1,b-1) + combinacao(a - 1, b)
    
setores = []

quantidade_setores = int(input())
minimo_possibilidades = int(input())

for setor in range(quantidade_setores):
    n = int(input())
    k = int(input())
    resultado = combinacao(n, k)
    setores.append(resultado)

print("Relatório dos escudos de Norte:")
aprovados = 0
for i in range(quantidade_setores):
    if setores[i] >= minimo_possibilidades:
        print(f"Setor {i + 1}: {setores[i]} possibilidade(s). Variedade suficiente!")
        aprovados += 1
    else:
        print(f"Setor {i + 1}: {setores[i]} possibilidade(s). Precisa de mais alternativas!")

print(f"Setores que atingiram a meta: {aprovados} de {quantidade_setores}.")

if aprovados == quantidade_setores:
    print("Tudo pronto! O planejamento dos escudos foi aprovado!")
else:
    print("Norte precisa revisar o planejamento!")