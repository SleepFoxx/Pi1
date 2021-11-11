zoznam_cisel = [1,5,9,7,8,5,4,4,78,89,45,4,]
zoznam_prazdny = []
zoznam_pismen = ["a","c","f","g"]
zoznam_mix = [14,"slovo",55,"@"]
zoznam = list(range(3))
print(zoznam_cisel[4])          #vypíše zo zoznamu podla indexu
print(zoznam_mix[-1])           #ked je v indexe záporné číslo, ide to od zadu ------------ index vždy začína 0 čiže 1č. - 0 index atd. -1 index = posledné číslo

neorezany_zoznam = list(range(10))
print(neorezany_zoznam)
print(neorezany_zoznam[0:5])    #neorezany zoznam od 0 do 5
print(neorezany_zoznam[2:8])    # od 2 do 8
print(neorezany_zoznam[1:7:2])  # medzi 1 a 7 začínajúc od 2
print(neorezany_zoznam[2:9:3])  # medzi 2 a 9 od 3

#Velikost zoznamu
x = [5,8,1,3,"slovo",6,7]
print(len(x))                   #vypíše len počet večí v zozname

#prechadzanie zoznamu
#1.
zoznam_prvkov = ["jablko","hruška","banán"]
for prvok in zoznam_prvkov:      #za in aký zoznam,,,,, za for ako pomenujeme jeden prvok
    print(prvok)

#2.
for index in range(len(zoznam_prvkov)):
    print(zoznam_prvkov[index])

#metódy pre zoznamy
myList = [1,5,8,55,500]
#append ------> pridá na koniec listu nový prvok
myList.append(99)
print(myList)
#pop ------> odstráni posledné číslo zo zoznamu
myList.pop()
print(myList)


#funkcie pre zoznamy
#len
#min/max
myList2 = [1,54,7,2,74,-10]
print("Minimum",min(myList2))               #minimum z prvkov
print("Maximum",max(myList2))               #maximum z prvkov
print("suma",sum(myList2))                  #spočítať všetky prvky
print(sorted(myList2))                      #zoradené