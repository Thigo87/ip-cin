DIRECOES = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

def movimentacao(movimento, posicao_atual):
    mov = DIRECOES[movimento]

    x_atualizado = posicao_atual[0] + mov[0]
    y_atualizado = posicao_atual[1] + mov[1]

    if not (0 <= x_atualizado <= 4):
        x_atualizado = posicao_atual[0]

    if not (0 <= y_atualizado <= 4):
        y_atualizado = posicao_atual[1]

    return x_atualizado, y_atualizado

print(movimentacao(">", [4, 3]))