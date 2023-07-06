frase = "hello. how are you? i'm fine, thank you."
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