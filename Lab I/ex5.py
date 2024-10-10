#Write a function that validates if a number is a palindrome.
def este_palindrom(numar):
    numar_str = str(numar)
    
    lungime = len(numar_str)
    
    mijloc = int(lungime / 2)
    
    for i in range(mijloc):
        if numar_str[i] != numar_str[lungime - i - 1]:
            return False
    return True

numar = int(input("Introdu un număr: "))
if este_palindrom(numar):
    print(f"Numărul {numar} este palindrom.")
else:
    print(f"Numărul {numar} nu este palindrom.")