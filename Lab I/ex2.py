#Write a script that calculates how many vowels are in a string.
string = input("String: ")

vocale = "aeiouAEIOU"

n_vocale = 0

for char in string:
    if char in vocale:  
        n_vocale += 1

print(f"Vocalele din string: {n_vocale}")
