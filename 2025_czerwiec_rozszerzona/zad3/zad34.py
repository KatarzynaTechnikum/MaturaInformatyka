path = "dane_przyklad.txt"
path = "dane.txt"

with open(path, "r", encoding="utf-8") as file:
    z = file.read()

# print(z)
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

# print(liczby)
# Spośród wszystkich numerów telefonów podaj te, które składają się z najmniejszej liczby
# różnych cyfr.

liczby_r = []
mini = 10
for i in liczby:
    if mini == len(set(i)):
        liczby_r.append(i)
    elif  len(set(i)) < mini:
        mini = len(set(i))
        liczby_r.clear()
        liczby_r.append(i)
print(liczby_r)
with open("wyniki3_4.txt", "w", encoding="utf-8") as file:
    for i in range(len(liczby_r)):
            file.write(f"{liczby_r[i]}\n")