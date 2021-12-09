#generovanie nahodneho čisla

import random 
#plocha

hracia_plocha = ["-","-","-",
                "-","-","-",
                "-","-","-"]
#definovanie hraca a hry

hrac = "X"
hrabezi = True
vyherca = None
#definicia plochy

def zobrazenie_plochy(hracia_plocha):
    print(hracia_plocha[0]+" | " + hracia_plocha[1] + " | " + hracia_plocha[2])
    print("----------")
    print(hracia_plocha[3]+" | " + hracia_plocha[4] + " | " + hracia_plocha[5])
    print("----------")
    print(hracia_plocha[6]+" | " + hracia_plocha[7] + " | " + hracia_plocha[8])
#input od hráča + kontrola či miesto už nieje obsadené

def Inputhraca(hracia_plocha):
    inp = int(input("Zadaj číslo od 1 po 9: "))
    if inp >= 1 and inp <= 9 and hracia_plocha[inp-1] == "-":
        hracia_plocha[inp-1] = hrac 
    else:
        "Zadal si zlé číslo alebo je miesto už zabrané!"

#skontrolovanie kto vyhral alebo prehral
def horizontalnakontrola(hracia_plocha):
    global vyherca
    if hracia_plocha[0] == hracia_plocha[1] == hracia_plocha[2] and hracia_plocha[1] != "-":
        vyherca = hracia_plocha[0]
        return True
    elif hracia_plocha[3] == hracia_plocha[4] == hracia_plocha[5] and hracia_plocha[3] != "-":
        vyherca = hracia_plocha[3]
        return True
    elif hracia_plocha[6] == hracia_plocha[7] == hracia_plocha[8] and hracia_plocha[6] != "-":
        vyherca = hracia_plocha[6]
        return True

def vertikalnakontrola(hracia_plocha):
    global vyherca
    if hracia_plocha[0] == hracia_plocha[3] == hracia_plocha[6] and hracia_plocha[0] != "-":
        vyherca = hracia_plocha[0]
        return True 
    elif hracia_plocha[1] == hracia_plocha[4] == hracia_plocha[7] and hracia_plocha[1] != "-":
        vyherca = hracia_plocha[1]
        return True 
    elif hracia_plocha[2] == hracia_plocha[5] == hracia_plocha[8] and hracia_plocha[2] != "-":
        vyherca = hracia_plocha[2]
        return True

def kontrolaremiza(hracia_plocha):
    global hrabezi
    if "-" not in hracia_plocha:
        zobrazenie_plochy(hracia_plocha)
        print("Je to remíza!")
        hrabezi = False

def diagonalnakontrola(hracia_plocha):
    global vyherca
    if hracia_plocha[0] == hracia_plocha[4] == hracia_plocha[8] and hracia_plocha[0] != "-":
        vyherca = hracia_plocha[0]
        return True 
    elif hracia_plocha[2] == hracia_plocha[4] == hracia_plocha[6] and hracia_plocha[2] != "-":
        vyherca = hracia_plocha[2]
        return True

#vyhodnotenie hraca 
def skontrolovanievyhry():
    global hrabezi  
    if horizontalnakontrola(hracia_plocha) or vertikalnakontrola(hracia_plocha) or diagonalnakontrola(hracia_plocha):
        print("Výherca je :",vyherca)
        hrabezi = False

#prehodenie hráča
def vymenahraca():
    global hrac 
    if hrac == "X":
        hrac = "0"
    else:
        hrac = "X"
#počítač 
def počítač(hracia_plocha):
    while hrac == "0":
        pozicia = random.randint(0,8)
        if hracia_plocha[pozicia] == "-":
            hracia_plocha[pozicia] = "0"
            vymenahraca()

#spustenie celeho programu
while hrabezi:
    zobrazenie_plochy(hracia_plocha)
    Inputhraca(hracia_plocha)
    skontrolovanievyhry()
    kontrolaremiza(hracia_plocha)
    vymenahraca()
    počítač(hracia_plocha)
    skontrolovanievyhry()
    kontrolaremiza(hracia_plocha)
zobrazenie_plochy(hracia_plocha)