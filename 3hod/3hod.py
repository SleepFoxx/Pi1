"""""
cislo = 100
while (cislo >= 0):
    print (cislo)
    cislo = cislo - 1


start = 10
koniec = 0
while start >= koniec:
    if start == 5:
        start -= 1
        continue
    print(start)
    start -= 1

start = int(input("Zadaj odkial začneme počítať"))
koniec = int(input("Zadaj pokial budem počítať"))
while start <= koniec:
    if start % 3 == 0:
        print(start)
    start += 1
for premenna in range(10):
    print(premenna)

samohlasky = "aáeéěiíoóuúyý"
slovo = input("Zadaj slovo")
obsahuje_samohlasky = False
for znak in slovo:
    if znak in samohlasky:
        obsahuje_samohlasky = True
        break

if obsahuje_samohlasky == True:
    print("Sloho obsahuje samohlasky")
else:
    print("Slovo neobsahuje samohlasky")

int = slovo =input("Zadaj slovo")
count = 0
count2 = 0
count3 = 0
count4 = 0
samohlasky = "a,á,e,é,ě,i,í,o,ó,u,ú,y,ý"
čísla = "1,2,3,4,5,6,7,8,9,0"
spoluhlasky = "b,d,ď,dz,dž,g,h,z,ž,v,p,t,ť,c,č,k,ch,s,š,f,m,n,ň,l,ľ,r,j"
for znak in slovo:
    if znak in spoluhlasky:
         count = count+1
    elif znak in čísla:
         count2 = count2+1
    elif znak in spoluhlasky:
        count3 = count3+1
    else:
        count4 = count4+1
print("Počet spoluhlások je:", count)
print("Počet čísel je:",count2)
print("Počet samohlások je:",count3)
print("Ostatných znakov je:",count4)

prvyzačiatok = int(input("Zadajte začiatok prvého invetvalu"))
prvykoniec = int(input("Zadajte koniec prvého intervalu"))
druhyzačiatok = int(input("Zadajte začiatok druhého intervalu"))
druhykoniec = int(input("Zadajte koniec druhého intervalu"))
prvyinterval = interval = ([prvyzačiatok, prvykoniec])
druhyinterval = interval = ([druhyzačiatok, druhykoniec])
print(prvyinterval)
print(druhyinterval)

riadky = int = input("Zadaj počet riadkov:")
stĺpce = int =input("Zadaj počet stĺpcov:")
for i in range(0, stĺpce):
    for j in range(0, riadky):
        print("*",end="")
    print()

for j in range(0,4):
    for i in range(0,j+1):
        print("*",end="")
    print()

výška=4
for j in range(0,4):
    for i in range(0,výška ):
        print("*", end="")
    výška = výška - 1
    print()

výška = 4
for j in range (0,výška):
    for i in range (0,výška):
        print("",end="")
    print()
"""
a = 8
for i in range(0, 5):
    for j in range(0, a):
        print(end=" ")
  #  a = a - 1 / 2
    for j in range(0, i+1):
        print("* ", end="")
    print()