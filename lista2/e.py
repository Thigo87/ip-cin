desfecho = False

qnt_ataques = int(input())

n_ataques = 0

print("Quando percebi que contara oito mortes, senti o peso da minha própria lenda")
if qnt_ataques > 0:
    while qnt_ataques > 0 and desfecho == False:
        qnt_ataques -= 1
        n_ataques += 1
        print("Preciso encontrar esse mapa a qualquer custo, nem que seja a última coisa que eu faça com esta vida!")
        companheiro = input()
        if companheiro == "cao perrito":
            print("Olha só... de todas as criaturas do mundo, justo você tinha que decidir me seguir com esse rabo abanando?")
            N = int(input())
            n_divisiveis = 0
            for i in range(0, N):
                num = int(input())
                if num % 3 == 0:
                    n_divisiveis += 1
            if n_divisiveis == N:
                desfecho = True
                print("Bom trabalho, meu garoto! Quem diria que um cãozinho tão pequeno seria o grande herói do dia?")
        elif companheiro == "kitty patamansa":
            print("Kitty... Olhar para você de novo só me faz lembrar que, entre todas as minhas nove vidas, o meu maior erro foi ter deixado você esperando.")
            item = input()
            if item == "chapeu do gato" or item == "bota do gato":
                desfecho = True
                print("Impressionante, Kitty... Sempre soube que você era rápida, mas admito que nada fica melhor nas mãos da melhor ladra de Tão Tão Distante do que um presente para mim.")
        else:
            stop = False
            while stop == False:
                frase = input()
                if "Desfecho" in frase:
                    desfecho = True
                    stop = True
                elif "Morte" in frase:
                    stop = True
else:
    print("Até logo, velho amigo... É bom saber que finalmente posso respirar fundo e apenas viver o dia de hoje.")

if desfecho:
    print("Parece que essa família de ursos e sua cachinhos acabam de provar do verdadeiro felino de botas!")
    frase_gato = input()
    if "coragem" in frase_gato.lower():
        print("A verdadeira vitória não está em vencer a morte, mas em encará-la de frente e escolher lutar por cada segundo desta vida!")
    else:
         print("Pode levar minha espada e meu chapéu... Eu lutei até o fim, mas hoje a lenda finalmente descansa.")
else:
    if n_ataques > 0 and not desfecho:
        print("Pode levar minha espada e meu chapéu... Eu lutei até o fim, mas hoje a lenda finalmente descansa.")