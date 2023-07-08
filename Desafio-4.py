def formatar_frase(frase):

    nova_frase = ""
    deve_ser_maiusculo = True

    for letra in frase:
        if deve_ser_maiusculo and letra != " ":
            nova_frase += letra.upper()
            deve_ser_maiusculo = False
        else:
            nova_frase += letra

        if letra in ["?", "."]:
            deve_ser_maiusculo = True

    return nova_frase

frase = "hello. how are you? i'm fine, thank you."

print(formatar_frase(frase))