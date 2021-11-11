slovo = input("Vlož slovo")
def palindrom(slovo):
    if slovo == slovo[::-1]:
        print("Palindrom")
    else:
        print("Nie je palindrom")
palindrom(slovo)


str = input("Zadaj slovo")
def otocene_slovo(str):
    str1 = ""
    for i in str:
        str1 + i + str1
    return  str1
if str == otocene_slovo(str):
    print("Slovo je palindrom")
else:
    print("Slovo nie je palindrom")
