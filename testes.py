def combinacao(a, b):
    if b == 0 or a == b:
        return 1
    else:
        return combinacao(a-1,b-1) + combinacao(a - 1, b)
    
print(combinacao(5,2))