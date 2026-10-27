def somatorio(num):
    if num == 1:
        return num
    return num + somatorio(num - 1)

n = int(input("Digite um numero: "))
print(somatorio(n))

#=======================================

def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)

a = int(input())
b = int(input())

print(potencia(a,b))