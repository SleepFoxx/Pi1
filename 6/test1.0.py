

začiatok = []
z = -1
počet_suborov = int(input("Zadaj koľko súborov chceš vytvoriť: "))
slovo_subor = [z + 1]
with open("./basnicka.txt", encoding="utf-8") as subor:
    for riadok in subor:
        začiatok += riadok.split()
x = 0
basen = len(začiatok)
for i in range(počet_suborov):
    if i >= basen:
        x = i - basen
    open("%s.txt" % i, "w", encoding="utf-8").write(začiatok[x])