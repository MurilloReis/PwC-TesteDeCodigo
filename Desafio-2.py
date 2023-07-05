frase_inicial = "Hello, World!"

frase_final = ""

for index in range(len(frase_inicial)):
    letra = frase_inicial[index]
    if letra not in frase_final:
        frase_final += letra