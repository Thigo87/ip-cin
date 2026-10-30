l = ["m", "a", "t", "d"]
d = {}

n = len(l)
for i in range(n):
    for j in range(n-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

for i in range(n):
    d.update({i : l[i]})

print(l)
print(d)