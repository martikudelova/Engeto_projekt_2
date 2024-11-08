"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martina Kudelova
email: marti.kudelova@gmail.com
discord: martina_44769
"""
import random
import time
import os

# kontrola, jestli existuje soubor a jeho případné vytvoření
if os.path.exists('statistiky.txt'):
    with open("statistiky.txt", mode='r') as statistiky_txt:
        statistiky_list = statistiky_txt.read().splitlines()
else:
    pocatecni_text = "prumer_pokusy 0\nprumer_cas 0\npokusy_min 0\ncas_min 0\npocet_her 0\ncelkove_pokusy 0\ncelkovy_cas 0"
    with open("statistiky.txt", mode='w') as statistiky_txt:
        statistiky_txt.write(pocatecni_text)
    statistiky_list = pocatecni_text.splitlines()

oddelovac = 47 * "-"
pocet_pokusu = 0

def vygeneruj_tajne_cislo():
    """
    Vygeneruje tajne cislo, ktere nezacina nulou a ma 4 unikatni cisla.
    """
    prvni = random.choice("123456789") 
    cislice = [c for c in "0123456789" if c != prvni] 
    zbytek = random.sample(cislice, 3)
    cislo = prvni + ''.join(zbytek)
    return cislo

def zadej_cislo():
    """
    Vyzaduje input, kontroluje správnost inputu a pocita pocet pokusu.
    """
    global pocet_pokusu
    while True: # opakuje input, dokud není nalezeno správné číslo
        hadane_cislo = input()
        if zkontroluj_cislo(hadane_cislo):   # kontroluje číslo, dokud funkce zkontroluj_cislo nevrátí True
            print(">>>", hadane_cislo)
            pocet_pokusu += 1
            return hadane_cislo

def zkontroluj_cislo(cislo: str) -> bool:
    """
    Kontroluje spravnost uzivatelem zadavanych cisel.
    """
    if not cislo.isdecimal():
        print("******Enter digits only ******")
        print(oddelovac)
        return False
    if len(cislo) != 4 or len(set(cislo)) != 4:
        print("******Number must be 4 unique digits long******")
        print(oddelovac)
        return False
    if cislo.startswith("0"):
        print("******Number cannot start with a 0******")
        print(oddelovac)
        return False
    return True

def porovnej_cisla(hadane_cislo, tajne_cislo):
    """
    Porovnava tajne cislo s inputem od uzivatele, pocita bulls a cows.
    """
    bulls = 0
    cows = 0
    for i in range(4):
        if hadane_cislo[i] == tajne_cislo[i]:
            bulls += 1
        elif hadane_cislo[i] in tajne_cislo:
            cows += 1    
    if bulls == 4:
        print(f"Correct, you've guessed the right number in {pocet_pokusu} guesses.")
        print(oddelovac)
        print("That's amazing!")
        return True
    else:
        if bulls != 1 and cows != 1:
            print(bulls, "bulls", cows, "cows")
        elif bulls == 1 and cows != 1:
            print(bulls, "bull", cows, "cows")
        elif bulls != 1 and cows == 1:
            print(bulls, "bulls", cows, "cow")
        elif bulls == 1 and cows == 1:
            print(bulls, "bull", cows, "cow")
        print(oddelovac)
        return False
    
def vytahni_statistiky():
    """
    Vytahuje statistiky ze souboru a ukládá je do proměnných.
    """
    prumer_pokusy = float(statistiky_list[0].split()[1])
    prumer_cas = float(statistiky_list[1].split()[1])
    pokusy_min = int(statistiky_list[2].split()[1])
    cas_min = float(statistiky_list[3].split()[1])
    pocet_her = int(statistiky_list[4].split()[1])
    celkove_pokusy = int(statistiky_list[5].split()[1])
    celkovy_cas = float(statistiky_list[6].split()[1])
    return prumer_pokusy, prumer_cas, pokusy_min, cas_min, pocet_her, celkove_pokusy, celkovy_cas

def aktualizuj_statistiky(cas):
    """
    Vypočte nové statistiky a uloží je do souboru a do globální proměnné.
    """
    prumer_pokusy, prumer_cas, pokusy_min, cas_min, pocet_her, celkove_pokusy, celkovy_cas = vytahni_statistiky()
    pocet_her += 1
    celkove_pokusy += pocet_pokusu
    celkovy_cas += cas
    prumer_pokusy = celkove_pokusy / pocet_her
    prumer_cas = celkovy_cas / pocet_her
    if pokusy_min == 0 or pokusy_min > pocet_pokusu:
        pokusy_min = pocet_pokusu
    if cas_min == 0 or cas_min > cas:
        cas_min = cas
    with open("statistiky.txt", mode='w') as statistiky_txt:
        aktualizovany_text = f"prumer_pokusy {prumer_pokusy}\nprumer_cas {prumer_cas}\npokusy_min {pokusy_min}\ncas_min {cas_min}\npocet_her {pocet_her}\ncelkove_pokusy {celkove_pokusy}\ncelkovy_cas {celkovy_cas}"
        statistiky_txt.write(aktualizovany_text)
    global statistiky_list
    statistiky_list = aktualizovany_text.splitlines()
    
print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(oddelovac)
print("Enter a number:")
print(oddelovac)

pocatecni_cas = time.time()
tajne_cislo = vygeneruj_tajne_cislo()

while True: # opakuje kód, dokud není podmínkou if, ukončen program
    hadane_cislo = zadej_cislo()
    if porovnej_cisla(hadane_cislo, tajne_cislo): # když se vrátí True z funkce porovnej_cisla, aktualizují se statistiky a program se ukončí
        koncovy_cas = time.time()
        cas = koncovy_cas - pocatecni_cas
        minuty, sekundy = divmod(cas, 60)
        print(f"Time taken: {int(minuty)} min and {sekundy:.2f} sec")
        print(oddelovac)
        aktualizuj_statistiky(cas)
        prumer_pokusy, prumer_cas, pokusy_min, cas_min, pocet_her, celkove_pokusy, celkovy_cas = vytahni_statistiky()
        print(f"Number of games: {pocet_her}")
        print(f"Average number of attempts: {prumer_pokusy:.1f}")
        minuty, sekundy = divmod(prumer_cas, 60)
        print(f"Average time: {int(minuty)} min and {sekundy:.0f} sec")
        print(f"Fastest game in number of attempts: {pokusy_min}")
        minuty, sekundy = divmod(cas_min, 60)
        print(f"Fastest game in time: {int(minuty)} min and {sekundy:.0f} sec")
        break
