login = input()
senha = input()

pontos = 0

print("Byte irá julgar a sua senha.")

tamanho = len(senha)

if tamanho < 8 or " " in senha or senha.isnumeric() or ('0' not in senha and '1' not in senha and '2' not in senha and '3' not in senha and '4' not in senha and '5' not in senha and '6' not in senha and '7' not in senha and '8' not in senha and '9' not in senha):
    print("Essa senha nem chega perto do que eu aceito. Tente de novo.")
else:
    print("Vamos fazer a contagem dos pontos.")
    if tamanho > 14:
        print("Que senha grande! Não seria difícil esquecer dela.")
    if tamanho > 11:
        pontos += tamanho - 11
    if ("A" in senha or "B" in senha or "C" in senha or "D" in senha or "E" in senha or "F" in senha or "G" in senha or "H" in senha or "I" in senha or "J" in senha or "K" in senha or "L" in senha or "M" in senha or "N" in senha or "O" in senha or "P" in senha or "Q" in senha or "R" in senha or "S" in senha or "T" in senha or "U" in senha or "V" in senha or "W" in senha or "X" in senha or "Y" in senha or "Z" in senha or "Ç" in senha) and ("a" in senha or "b" in senha or "c" in senha or "d" in senha or "e" in senha or "f" in senha or "g" in senha or "h" in senha or "i" in senha or "j" in senha or "k" in senha or "l" in senha or "m" in senha or "n" in senha or "o" in senha or "p" in senha or "q" in senha or "r" in senha or "s" in senha or "t" in senha or "u" in senha or "v" in senha or "w" in senha or "x" in senha or "y" in senha or "z" in senha or "ç" in senha):
        pontos += 5
    if "@" in senha:
        pontos += 1
    if "_" in senha:
        pontos += 1
    if "&" in senha:
        pontos += 1
    if "%" in senha:
        pontos += 1
    if "#" in senha:
        pontos += 1
    if login in senha or login.upper() in senha or login.lower() in senha or login.capitalize() in senha or login.upper() in senha.upper():
        pontos -= 10
        print("Olha o que eu encontrei aqui, não deixarei isso passar tão fácil.")
    
    if pontos < 1:
        print(f"Infelizmente terá que mudar sua senha, é para o seu bem.\nMelhore sua senha em {abs(1 - pontos)} ponto(s) e ela será suficiente.")

    elif 0 < pontos < 11:
        print("Pode manter a sua senha, ela parece adequada.")
    
    elif pontos > 10:
        print("Parabéns! Nem o maior hacker do mundo encontraria uma senha assim.")