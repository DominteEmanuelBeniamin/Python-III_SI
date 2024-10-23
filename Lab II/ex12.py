def group_by_rhyme(lista_cuvinte):
    dictionar_rime = {}
    
    for cuvant in lista_cuvinte:
        ultimele_doua = cuvant[-2:]
        if ultimele_doua in dictionar_rime:
            dictionar_rime[ultimele_doua].append(cuvant)
        else:
            dictionar_rime[ultimele_doua] = [cuvant]
    
    return list(dictionar_rime.values())

rezultat = group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte'])
print(rezultat)
