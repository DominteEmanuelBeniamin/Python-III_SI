# Srieti o functie care primeste ca parametru o expreise matematica cu paranteze rotunde si verifica daca parantezarea este sau nu corecta
# Exemplu 1: "6+8*(5+3/2-1+6/(3+9)-7*(5+7/3))" va returna True
# Exemplu 2: "8-4*(3+7/8+4/(5-9)" va returna False

def verifica_expresie(expresie):
    paranteze = 0
    for caracter in expresie:
        if caracter == "(":
            paranteze += 1
        elif caracter == ")":
            paranteze -= 1
    if paranteze != 0:
         return False
    return True


        
expresie = input("Introdu expresia matematica: ")
print(verifica_expresie(expresie))