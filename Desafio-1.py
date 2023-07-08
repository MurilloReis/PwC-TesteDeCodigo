def inverter_frase(frase):

    frase = frase.split(" ")
    frase_invertida = frase.reverse()
    frase_invertida = " ".join(frase)

    return frase_invertida

teste = "hello, World! OpenAI is amazing."

print(inverter_frase(teste))