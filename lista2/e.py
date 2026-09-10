desfecho = False

qnt_ataques = int(input())

print("Quando percebi que contara oito mortes, senti o peso da minha própria lenda")
if qnt_ataques > 0:
    while True: #AJUSTAR ESSE WHILE    
        companheiro = input()
        if companheiro == "cao perrito": #Ajustar o final
            N = int(input())
            n_divisiveis = 0
            for i in range(0, N):
                num = int(input())
                if num % 3 == 0:
                    n_divisiveis += 1
            if n_divisiveis == N:
                desfecho = True
        elif companheiro == "kitty patamansa": #Ajustar o final
            item = input()
            if item == "chapeu do gato" or item == "bota do gato":
                desfecho = True
        else:
            stop = False
            while stop == False:
                frase = input()
                if "desfecho" in frase.lower():
                    desfecho = True
                elif "morte" in frase.lower():
                    pass #Vai para o próximo ataque

#Ao final, o gato vai falar uma frase