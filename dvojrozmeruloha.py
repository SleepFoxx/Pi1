cierny_riadok = ["█"," ","█"," ","█"," ","█"," "]
biely_riadok = [" "," █"," ","█"," ","█"," "," "]
sachovnica = []
for i in range(4):
    for znak in cierny_riadok:
        print(znak, end="")
    print(sep="")
    for y in biely_riadok:
        print(y, end="")
    print("")