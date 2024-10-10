#Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.
def extrage_numar(text):
    numar = ""
    
    for caracter in text:
        if caracter.isdigit():
            numar += caracter
        elif numar:
            break
    
    return int(numar) if numar else None

text = input("Introdu un text: ")
numar_extras = extrage_numar(text)
if numar_extras is not None:
    print(f"Primul număr extras din text este: {numar_extras}")
else:
    print("Nu a fost găsit niciun număr în text.")
