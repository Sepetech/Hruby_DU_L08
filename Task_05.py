def pocitadlo_slov(zdroj_dat, slovo):
    try:
        with open(zdroj_dat, 'r') as file:
            text = file.read().lower()
            frequency = text.count(slovo.lower())
            return frequency
    except FileNotFoundError:
        print("Soubor nenalezen.")
        return None

zdroj_dat = input("Zadej nazev souboru: ")
slovo = input("Zadej hledane slovo: ")

frequency = pocitadlo_slov(zdroj_dat, slovo)

if frequency is not None:
    print(f"Slovo '{slovo}' se v souboru opakuje {frequency} krát.")
