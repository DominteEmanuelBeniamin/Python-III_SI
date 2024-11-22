import sys
import os

def numara_caractere(file_name):
    if not os.path.exists(file_name):
        print("Eroare: fisierul nu exista.")
        return
    
    with open(file_name, 'r') as f:
        text = f.read().lower()
    
    cuvinte = text.split()
    dictionar = {}
    
    for cuv in cuvinte:
        cuv_fara_spec=''.join(e for e in cuv if e.isalnum())
        caractere_dif=len(set(cuv_fara_spec))
        if cuv_fara_spec not in dictionar:
            dictionar[cuv_fara_spec] =  caractere_dif

    for cuv, caractere in sorted(dictionar.items()):
        print(f"{cuv} - {caractere}" )

if __name__ == '__main__':
    if len(sys.argv) !=2:
        print("Eroare: Foloseste script.py <nume_fisier>, Ex: script.py a.txt unde a.txt este fisierul de citire")
    else:
        numara_caractere(sys.argv[1])    

