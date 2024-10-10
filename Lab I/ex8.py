#Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.

def numara_cuvinte(text):
    return len(text.split())

text = input("Introdu un text: ")
print(f"Numărul de cuvinte în text este: {numara_cuvinte(text)}")
