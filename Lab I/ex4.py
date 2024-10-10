#Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

input_sir = input("UpperCamelCase: ")

sir_final = ""

for caracter in input_sir:
    if caracter.isupper():  
        if sir_final:  
            sir_final += "_"
        sir_final += caracter.lower()  
    else:
        sir_final += caracter  

print("Șirul convertit:", sir_final)
