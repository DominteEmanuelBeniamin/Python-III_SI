# Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
def operatii_liste(a, b):
    intersectie = list(set(a) & set(b))
    reuniune = list(set(a) | set(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))
    return (intersectie, reuniune, a_minus_b, b_minus_a)

a = [int(x) for x in input("Lista a: ").split()]
b = [int(x) for x in input("Lista b: ").split()]

rezultat = operatii_liste(a, b)

print("Intersecție:", rezultat[0])
print("Reuniune:", rezultat[1])
print("a - b:", rezultat[2])
print("b - a:", rezultat[3])
