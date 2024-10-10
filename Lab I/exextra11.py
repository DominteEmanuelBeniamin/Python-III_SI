#Cate vocale si consoane sunt intr-un text dat?

string = input("String: ")

vocale = "aeiouAEIOU"

n_vocale = 0
n_consoane = 0

for char in string:
    if char in vocale:  
        n_vocale += 1
    else: 
        n_consoane += 1

print(f"Vocalele din string: {n_vocale}, Consoanele din string: {n_consoane}")
