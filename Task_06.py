# Otevrit soubor pro cteni
with open("zdroj_dat.txt", "r") as file:
    # Precist obsah
    text = file.read()

# Dotaz na uzivatele
hledane_slovo = input("Zadej hledane slovo: ")
nahradni_slovo = input("Zadej, za co se ma slovo nahradit: ")

# Vymena slov
new_text = text.replace(hledane_slovo, nahradni_slovo)

# Otevreni souboru pro zapis
with open("nahrada.txt", "w") as file:
    # Zapis noveho textu
    file.write(new_text)
