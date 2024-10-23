def combina_liste(*liste):
    lungime_maxima = max(len(lista) for lista in liste)
    rezultat = []
    
    for i in range(lungime_maxima):
        tuplu = tuple(lista[i] if i < len(lista) else None for lista in liste)
        rezultat.append(tuplu)
    
    return rezultat

rezultat = combina_liste([1, 2, 3], [5, 6, 7], ["a", "b", "c"])
print(rezultat)
