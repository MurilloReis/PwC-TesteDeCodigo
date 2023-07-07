def verificar_anagrama_de_palindromo(palavra):
    caracteres_unicos = set(palavra)

    lista_simetria_caracteres = []
    for caracter in caracteres_unicos:
        lista_simetria_caracteres.append(palavra.count(caracter) % 2)