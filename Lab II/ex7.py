def gaseste_palindrome(lista):
    count = 0
    max_palindrom = None
    
    for numar in lista:
        if str(numar) == str(numar)[::-1]:
            count += 1
            if max_palindrom is None or numar > max_palindrom:
                max_palindrom = numar
    
    return (count, max_palindrom)

lista_numere = list(map(int, input("Introdu numere separate prin spatii: ").split()))
rezultat = gaseste_palindrome(lista_numere)
print(rezultat)
