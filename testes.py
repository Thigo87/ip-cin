def decrypt(frase, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    nova_frase = ""
    for letra in frase:
        if letra == " ":
            nova_frase += " "
        else:
            nova_frase += alfabeto[alfabeto.index(letra) - chave]
    return nova_frase 

def montagem_inventario(string):
    catalogo = {"arma" : ['cajado', 'machado grande', 'adaga', 'adaga dupla'], 
                "utilidade" : ['grimorio', 'escudo de madeira', 'alaude', 'ferramentas de ladrao'], 
                "consumivel" : ['pergaminho oculto', 'racao de viagem', 'pocao de cura', 'bomba de fumaca']}
    
    string_criptografada, chave_da_cifra, poder_do_item = string.split(" - ")
    item = decrypt(string_criptografada, int(chave_da_cifra))
    inventario = {}
    
    for tipo in catalogo:
        if item in catalogo[tipo]:
            inventario.update({item : {"tipo" : tipo, "poder" : poder_do_item}})
    
    return inventario

mago = {}
mago.update({"nome" : "Teste", "inventario":{}})
frase = ""
while frase != "pronto":
    frase = input()
    if frase != "pronto":
        mago["inventario"].update(montagem_inventario(frase))
    
print(mago)
