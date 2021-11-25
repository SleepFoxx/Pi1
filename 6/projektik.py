
slova = [input()]

subory = int(input("Zadaj počet súborov"))

for pismeno in slovo:
    with open("basnicka.txt")



def slovo_subor(a):
    a = -1
    print(slova[a + 1], file="basnicka0.txt")

with open("./basnicka.txt", encoding="UTF-8") as subor:
    for riadok in subor:
        slova += riadok.split()


for i in range(subory):
    with open ("./Pi1/basnicka0.txt" + slovo_subor, encoding="UTF-8", mode="w") as subor:
        print("Šak povedz ty ne?", file=subor)



for item in slova:
    with open("./basnicka.txt".format(item), "w") as f:
        f.write("This is my first line of code")
        f.write("\nThis is my second line of code with {} the first item in my list".format(item))
        f.write("\nAnd this is my last line of code")
