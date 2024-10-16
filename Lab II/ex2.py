# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def este_prim(numar):
    if numar < 2:
        return False
    for i in range(2, int(numar ** 0.5) + 1):
        if numar % i == 0:
            return False
    return True

def gaseste_prime(lista_numere):
    return [x for x in lista_numere if este_prim(x)]

lista_numere = list(map(int, input("Introduceți numerele separate prin spațiu: ").split()))
rezultat_prime = gaseste_prime(lista_numere)
print(f"Numerele prime din listă sunt: {rezultat_prime}")
