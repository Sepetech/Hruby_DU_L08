# Otevre zdrojovy soubor
with open('zdroj_dat.txt', 'r') as f:
    text = f.read()

# Nastaveni pocitadel
znak_pocet = 0
radek_pocet = 0
samohlaska_pocet = 0
souhlaska_pocet = 0
cislice_pocet = 0

# Overeni znaku
for char in text:
    znak_pocet += 1
    # Souhlaska/samohlaska
    if char.isalpha():
        if char.lower() in 'aeiou':
            samohlaska_pocet += 1
        else:
            souhlaska_pocet += 1
    # Cislice
    elif char.isdigit():
        cislice_pocet += 1

    # Novy radek
    if char == '\n':
        radek_pocet += 1

# Vytvoreni noveho souboru
with open('statistika.txt', 'w') as f:
    f.write("Number of characters: {}\n".format(znak_pocet))
    f.write("Number of lines: {}\n".format(radek_pocet))
    f.write("Number of vowels: {}\n".format(samohlaska_pocet))
    f.write("Number of consonants: {}\n".format(souhlaska_pocet))
    f.write("Number of digits: {}\n".format(cislice_pocet))
