d = {"um" : 1, "dois" : 2, "tres" : 3}
l = []
d_ajustado = {}
for item in d:
    l.append(d[item])
    
n = len(l)

for i in range(n):
    for j in range(n - i - 1):
        if l[j] < l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

for valor in l:
    for item in d:
        if valor == d[item]:
            d_ajustado.update({item : valor})
            
print(d_ajustado)
