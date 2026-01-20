# path = "dane_przyklad.txt"
path = "dane.txt"

with open(path, "r", encoding="utf-8") as file:
    z = file.read()


print(z)
z += " "
len_z = len(z)
liczby = []
biez = z[0]
for i in range(len_z-1):
    if z[i].isdigit() and z[i+1].isdigit():
        biez+=z[i+1]
    else:
        if len(biez) > 1:
            liczby.append(biez)
        biez = z[i+1]
print(liczby)
licznik = 0
for i in liczby:
    if i.startswith("50"):
        licznik += 1

with open("wyniki3_1.txt", "w", encoding="utf-8") as file:
    file.write(f"{licznik}")