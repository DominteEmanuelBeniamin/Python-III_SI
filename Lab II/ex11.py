def sorteaza_dupa_al_treilea_caracter(lista_tupluri):
    return sorted(lista_tupluri, key=lambda x: x[1][2])

lista = [('abc', 'bcd'), ('abc', 'zza')]
rezultat = sorteaza_dupa_al_treilea_caracter(lista)
print(rezultat)
