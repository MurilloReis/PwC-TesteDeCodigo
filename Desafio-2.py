def remover_repeticoes(frase):

    frase_final = ""

    for index in range(len(frase)):
        letra = frase[index]
        if letra not in frase_final:
            frase_final += letra
            
    return frase_final

frase_inicial = "Hello, World!"

print(remover_repeticoes(frase_inicial))