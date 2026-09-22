print("--- FASE 3: A MENSAGEM ---")
alfabeto = "abcdefghijklmnopqrstuvwxyz "
    
mensagem_codificada = "0 8 6 52 18 28 14 26"
mensagem = ""
    
mensagem_codificada = [int(char) for char in mensagem_codificada.split()]
print(mensagem_codificada)
mensagem_codificada = [alfabeto[(x // 2) % 27] if x % 2 == 0 else alfabeto[(x * 3 + 1) % 27] for x in mensagem_codificada]

print(mensagem_codificada)

mensagem = "".join(mensagem_codificada)
        
print(f'Mensagem decodificada: "{mensagem}"')