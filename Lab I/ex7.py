#Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
def numara_biti_de_1(numar):

    numar_binar = bin(numar)
    
    numar_biti_1 = numar_binar.count('1')
    
    return numar_biti_1

numar = int(input("Introdu un număr: "))
print(f"Numărul de biți de valoare 1 este: {numara_biti_de_1(numar)}")
