"""
zoznam = [1,2,3,4,5,6,7,8,9,10]
otoceny_zoznam = zoznam[::-1]
for i in otoceny_zoznam:
    print(i)


zoznam_ovocie = ["malina","banán",]
zoznam_zelenina = ["brokolica"]

while (True):
    print("Zadaj názov lubovoľného ovocia alebo zeleniny")
    vstup = input()
    if vstup in zoznam_ovocie:
        print("Zadal si ovocie")
    elif vstup in zoznam_zelenina:
        print("Zadal si zeleninu")
    else:
        print("Tvoje slovo nemám v zozname")
    print("Chceš zadať ďaľšie slovo? ano/nie")
    otazka = input()
    if otazka ==  "nie":
        exit()
"""


print("Zadavaj čísla a nakoniec zadaj iba ENTER pre ukončenie zadavania")
číslo = input("Zadaj číslo:")
zoznam = [číslo,]
while (True):
    číslo2 = input("Zadaj číslo:")
    zoznam.append(číslo2)
    if číslo2 == "":
        break
inde = (len(zoznam)) / 2
index = inde - 1


