# path = "dane_przyklad.txt"
path = "dane.txt"

with open(path, "r", encoding="utf-8") as file:
    z = file.read()
# Znajdź i wypisz wszystkie numery telefonów zaczynające się od cyfry 5 z pliku dane.txt
# w kolejności ich występowania w tym pliku.

print(z)
z += " "
len_z = len(z)
liczby = []
current = z[0]
for i in range(1, len_z):
    if z[i-1].isdigit() and z[i].isdigit():
        current+=z[i]
    else:
        if len(current) == 9:
            liczby.append(current)
        current = z[i]

print(liczby)


for n in liczby:
    if n.startswith("5"):
        print(n)

with open("wyniki3_3.txt", "w", encoding="utf-8") as file:

    for n in liczby:
        if n.startswith("5"):
            print(n)
            file.write(f"{n}\n")