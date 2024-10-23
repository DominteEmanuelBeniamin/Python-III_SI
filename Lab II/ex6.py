def gaseste_elemente_aparitii(x, *liste):
    dictionar = {}
    
    for lista in liste:
        for element in lista:
            dictionar[element] = dictionar.get(element, 0) + 1
    
    rezultat = [element for element, aparitii in dictionar.items() if aparitii == x]
    return rezultat

rezultat = gaseste_elemente_aparitii(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])
print(rezultat)
