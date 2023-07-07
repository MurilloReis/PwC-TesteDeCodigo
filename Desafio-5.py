def verificar_anagrama_de_palindromo(palavra):
    caracteres_unicos = set(palavra)

    lista_simetria_caracteres = []
    for caracter in caracteres_unicos:
        lista_simetria_caracteres.append(palavra.count(caracter) % 2)
    
    # return lista_simetria_caracteres.count(1) <= 1
    return "true" if lista_simetria_caracteres.count(1) <= 1 else "false"

teste = "racecar"

print(verificar_anagrama_de_palindromo(teste))