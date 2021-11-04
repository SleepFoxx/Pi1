#import turtle
#t = turtle.Turtle()

#Pretypovanie
#vek = int(input("Zadaj svoj vek: " ))
""""
a =int(input("Zadaj hodnotu a :"))
b =int(input("Zadaj hodnotu b : "))
scitanie = a+b
odcitanie = a-b
krat = a*b
if b == 0:
    print("Nulou sa nedelí!")
delene = a/b
else:
    print("a/b=", delene)
print("a+b=", scitanie)
print("a-b=",odcitanie)
print("a*b=", krat)

#+,-,*,/,**,% --> aritmeticke operatory
#print(10 ** 3) - mocnenie
#vysledok != - rovná, nerovná, <= >= - menší rovný, väčší rovný ==> logické operátory

vek = int(input("Zadaj svoj vek: "))
if vek >=18:
    print("Vstúp ďalej máš dosť rokov")
    print("Vitaj medzi nami")
elif vek <18:
    print("Si moc mladý dovidenia")

a = 20
b = 10
c = a
a = b
b = c
print(a)
print(b)


nálada = input("Ahoj, si štastný?")
zázemie = input("A si bohatý?")
if(nálada == "áno"):
    if (zázemie == "áno"):
        print("Gratulujem!")
    elif (zázemie == "nie"):
        print("Skús viac šetriť!")
else:
    if (zázemie == "nie"):
        print("Sorry, to mi je lúto :(")
    elif(zázemie == "áno"):
        print("Viac sa usmievaj :)")


username = input("Zadaj prihlasovacie meno")
password = input("Zadaj prihlasovacie meno")

if username == "root" and password == "password":
    print("Úspešne si sa prihlásil")
else:
    print("Zlé meno alebo heslo alebo vek")

"""
