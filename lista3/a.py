dwight = []
jim = []
stanley = []
phillips = []
michael = []

nome_do_vendedor = ''

while nome_do_vendedor.lower() != 'fim':
    nome_do_vendedor = input()
    
    if nome_do_vendedor.lower() != "fim":
        nome_da_empresa = input()
        
        if nome_do_vendedor == "Dwight":
            dwight.append(nome_da_empresa)    
        elif nome_do_vendedor == "Jim":
            jim.append(nome_da_empresa)
        elif nome_do_vendedor == "Stanley":
            stanley.append(nome_da_empresa)
        elif nome_do_vendedor == "Phillips":
            phillips.append(nome_da_empresa)
        else:
            michael.append(nome_da_empresa)

if len(dwight) > 0:
    print(f"Dwight : {dwight}")
else:
    print("Dwight fez zero vendas hoje. Mais sorte amanhã!")
    
if len(jim) > 0:
    print(f"Jim : {jim}")
else:
    print("Jim passou o dia fazendo pegadinhas e não concluiu nenhuma venda!")

if len(stanley) > 0:
    print(f"Stanley : {stanley}")
else:
    print("Stanley acabou dormindo em serviço, amanhã ele estará mais descansado!")
    
if len(phillips) > 0:
    print(f"Phillips : {phillips}")
else:
    print("Phillips se distraiu e acabou não fazendo vendas hoje!")

if len(michael) > 0:
    print("Michael realizou vendas hoje!")
    print(f"Michael : {michael}")
else:
    print("Michael não trabalhou como vendedor hoje, apenas foi um bom chefe.")