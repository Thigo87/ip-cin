def avaliacao_energia(num):
    if num == 0:
        return (1, 1)
    elif num == 1:
        return (1, 3)
    else:
        return (avaliacao_energia(num - 1)[1], (2 * avaliacao_energia(num - 1)[1]) + avaliacao_energia(num - 2)[1])
    
def avaliacao_brilho(num):
    if num == 0:
        return 1
    else:
        return (avaliacao_energia(num)[0]/avaliacao_energia(num)[1]) + avaliacao_brilho(num - 1)

print(avaliacao_energia(5))
print(avaliacao_brilho(3))

print(7/17)