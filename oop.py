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


class Car:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.milaage = mileage

car = Car(230, 10000)
print(car.max_speed, car.milaage)


class Car:
    pass


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.milaage = mileage

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 180, 12)
print("Vehicle name: ", school_bus.name, "Speed: ", school_bus.max_speed, "Mileage: ", school_bus.milaage)


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

bus = Bus("School Volvo", 180, 12)
print(bus.seating_capacity())


class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus("School Volvo", 180, 12)
car = Car("Volvo", 180, 12)
print("Color: ", bus.color, "Vehicle name:", bus.name, "Speed: ", bus.max_speed, "Mileage: ", bus.mileage)
print("Color: ", car.color, "Vehicle name:", car.name, "Speed: ", car.max_speed, "Mileage: ", car.mileage)


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount
    pass

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 12, 50)

print(type(school_bus))



class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(isinstance(School_bus, Vehicle))

class human:

    def __init__(self, name):
        self.name = name
        self.fatigue = 0

        
    
    def run(self, jednotka):
        if self.fatigue > 20:
            print( f"{self.name} je moc unaveny")
            return
        else:
            self.fatigue = jednotka * 1
            print(f"{self.name} bezi")
    

    def sleep(self, jednotka):
        self.fatigue = jednotka * 10
        print(f"{self.name} spi hodinu")
    
        
        

        
clovek = human("Jakub" )
clovek.run(25)
clovek.run(11)


import random


class Generator:
    def __init__(self):
        self.pridavne_mena = ["modry", "velky", "automatizovany", "hudobny", "najlepsi"]
        self.podstatne_mena = ["programator", "manazer", "hroch", "T-rex"]
        self.sloveso = ["upratoval", "spal", "varil" ]
        self.kde = ["v lese", "u babicky", "v praci"]

    def vygeneruj(self):
        a = random.choice(self.pridavne_mena)
        b = random.choice(self.podstatne_mena)
        c = random.choice(self.sloveso)
        d = random.choice(self.kde)
        print(f"{a} {b} {c} {d}")
        

generator = Generator()
generator.vygeneruj()
"""

class Auto:
    def __init__(self, color, SPZ):
        self.color = color
        self.SPZ = SPZ
    def zaparkuj(self):
        print(f"{self.SPZ} sa zaparkoval")
        return self.color, self.SPZ

auto = Auto("biela", "SYMONGAE123", )
auto1 = Auto("cervena", "ADAMGAE123", )
garaz = []
garaz.append(auto.zaparkuj())
garaz.append(auto1.zaparkuj())

print(f"V garazi je: ", garaz)






