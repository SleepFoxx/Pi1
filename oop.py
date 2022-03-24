"""
#trieda macka
class Cat:
    #konstruktor --> vykona sa pri vytvoreni instancie
    def __init__(self, name, vek):
        print("Konstruktor macka")
        self.name = name
        self.vek = vek

    def __str__(self):
        print(f"Meno macky je: {self.name} a vek je: {str(self.vek)}")
        return " "
        

    def zamnaukaj(self):
        print(self.name + " Miau")
    def zjedz(self, jedlo):
        print(self.name + " zjedla/zjedlo " + jedlo)


#instancie objektą klasy Cat
cat = Cat("Mica", 4)
#cat.meno = "Micka"

#volanie metody
cat.zamnaukaj()
cat.zjedz("rybu")

cat2 = Cat("Murko", 5)
cat2.zamnaukaj()

print(cat2)
"""
"""
class Car:
    def __str__(self):
        print(f"Nazov auta je: {self.name} a farba je: {self.color}")
        print(f"Rok vyroby je: {str(self.year)} a pocet miest je: {self.places}")
        print(f"Auto je nastartovane: {str(self.is_on)}")
        return " "
    
    def __init__(self, name, year, color, places, is_on):
        self.name = name
        self.color = color
        self.year = year
        self.places = places
        self.is_on = False
        
    def toggleMotor(self, state):
        self.is_on = state
        
            
    def go_front(self):
        print(self.name + " ide dopredu")
    def honk(self):
        print(self.name + ": TUUUUUUUUUUUUUUUUUUUUUUUUUUU")


car = Car("BMW", 2018, "black", 5, True)
car.honk()
car.go_front()
car.toggleMotor(True)
print(car)
car.toggleMotor(False)
print(car)
"""
"""
class Calculator:
    
    def add(self):
        return a + b
    def sub(self):
        return a - b
    def mul(self):
        return a * b
    def div(self):
        return a / b

calc = Calculator()

    
a = int(input("Zadaj prve cislo: "))
b = int(input("Zadaj druhe cislo: "))

print(f"{a} + {b} = {calc.add()}")
print(f"{a} - {b} = {calc.sub()}")
print(f"{a} * {b} = {calc.mul()}")
print(f"{a} / {b} = {calc.div()}")
"""
import random

hrany = int(input("Zadaj pocet hran: "))

class Dice:
    def __init__(self, hrany):
        self.hrany = hrany
    def hodkockou(self):
        return random.randint(1, self.hrany)


print(f"Kocka s {hrany}")

for i in range(0, 10):
    dice = Dice(hrany)
    print(dice.hodkockou())


    
    









