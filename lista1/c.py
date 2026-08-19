destino = input()
carisma = int(input())
futebol = int(input())
tenis = int(input())

if destino.upper() == "Tsinghua":
    if carisma >= 90:
        if futebol > tenis:
            print("Todos os torcedores do Santa Cruz passam a ter acesso ao intercâmbio para a Tsinghua University.")
        else:
            print("Os chineses gostam do Santa Cruz, mas preferem tênis de mesa e solicitam a criação do Santa Cruz Tênis de Mesa China.")
    else:
        print("Byte consegue fazer amigos na universidade, mas a paixão pelo Santa Cruz fica para a próxima.")
        
elif destino.upper() == "Shenzhen":
    if futebol >= 80:
        if carisma == 100:
            print("Todos os chineses passam a torcer para o Santa Cruz.")
        else:
            print("O Santa Cruz ganha um patrocínio de uma gigante de tecnologia de Shenzhen!")
            
    else:
        print("Byte falha em converter os chineses ao Santa Cruz, mas aproveita a viagem visitando Shenzhen.")
        
else:
    print("Passaporte invalido. Byte deve retornar a Recife.")