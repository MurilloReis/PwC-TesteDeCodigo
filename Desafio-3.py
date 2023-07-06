def buscar_palindromo(string):

    palindromos = []
    maior_palindromo = ""

    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromos.append(substring)
                if len(substring) > len(maior_palindromo):
                    maior_palindromo = substring

    return maior_palindromo