"""
cisla = [4,5,6,7]
print(cisla[3])

pole = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(pole[1][1])

print("----------------------------------------------------------------")
for riadok in pole:
    print(riadok)
    for prvok in riadok:
        print(prvok)

print("----------------------------------------------------------------")
"""
def vypisKinosalu(kinosala):
    for riadok in kinosala:
        print(riadok)


kinosala = []

for i in range(5):
    temp = []
    for i in range(10):
        temp2 = []
        for i in range(4):
            temp2.append(0)
        temp.append(temp2)
        kinosala.append(temp)
print()
kinosala[0][5] = 1
kinosala[2][4] = 1
vypisKinosalu(kinosala)
