def filtreaza_caractere(x=1, lista_strings=[], flag=True):
    rezultat = []
    
    for sir in lista_strings:
        if flag:
            rezultat.append([char for char in sir if ord(char) % x == 0])
        else:
            rezultat.append([char for char in sir if ord(char) % x != 0])
    
    return rezultat

x = int(input("Introdu numarul x: "))
lista_strings = input("Introdu lista de siruri separate prin spatii: ").split()
flag = input("Introdu valoarea flag (True/False): ").lower() == 'true'

rezultat = filtreaza_caractere(x, lista_strings, flag)
print(rezultat)
