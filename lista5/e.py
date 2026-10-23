INVENTÁRIO = {
    "nível": 0,
    'magias': [],
    'itens': {
        "pás": ["Pá do herói"],
    },
    'troféus': {
        'Capacete do Espectro': 0,
        'Capacete Gélido': 0
    }
}

ITENS = {
    "F": {"secao": "magias", "nome": "Varinha de Chamas", "mensagem": "O que é isso? Sinto um fogo emanando do fundo da minha alma…"},
    "V": {"secao": "magias", "nome": "Varinha de Gelo", "mensagem": "Uma magia nova é sempre bom!"},
    "P": {"secao": "pás", "nome": "Pá Espectral", "mensagem": "Uma pá transparente, que loucura!"},
    "p": {"secao": "pás", "nome": "Pá comum", "mensagem": "Mais uma para minha coleção."},
}

CHEFES = {
    "Specter Knight": {"capacete": "Capacete do Espectro", "nivel_minimo": 2},
    "Polar Knight": {"capacete": "Capacete Gélido", "nivel_minimo": 5},
}

DIRECOES = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}