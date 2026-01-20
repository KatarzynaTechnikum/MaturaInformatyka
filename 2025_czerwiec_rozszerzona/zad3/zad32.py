# path = "dane_przyklad.txt"
path = "dane.txt"

with open(path, "r", encoding="utf-8") as file:
    z = file.read()

# Podaj najczęściej występującą cyfrę w pliku dane.txt oraz liczbę jej wystąpień. W pliku
# jest jedna taka cyfra.

t = [0] * 10
for i in z:
    if i.isdigit():
        t[int(i)] += 1
poz = 0
ile = t[0]
for i in range(1,10):
    if t[i] >= ile:
        poz = i
        ile = t[i]
print(poz, ile)
with open("wyniki3_2.txt", "w", encoding="utf-8") as file:
    file.write(f"{poz} {ile}")