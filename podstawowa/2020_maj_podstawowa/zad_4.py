with open("liczby.txt") as p:
    dane = p.readlines()

n = len(dane)
for i in range(n):
    dane[i] = int(dane[i])

# print(dane)
wynik = open("wyniki4.txt", mode='w')

# zadanie 4.1.
wynik.write("Zadanie 4.1.\n")
c = 0
for i in dane:
    if i % 2 != 0: #sprawdznie nieparzystości
        c += 1
wynik.write(f"{c}\n")

# zadanie 4.2.
wynik.write("Zadanie 4.2.\n")

def suma_cyfr(liczba):
    liczba = str(liczba)
    suma = 0
    for i in liczba:
        suma += int(i)
    return suma == 11


for i in dane:
    if suma_cyfr(i):
        wynik.write(f"{i}\n")


# zadanie 4.3.
wynik.write("Zadanie 4.3.\n")


def czy_pierwsza4000(liczba):
    if liczba < 4000 or liczba > 5000:
        return False
    if liczba % 2 == 0 or liczba % 3 == 0:
        return False
    s = int(liczba ** 0.5 + 0.5)
    for i in range(5, s + 1, 2):
        if liczba % i == 0:
            return False
    return True


for i in dane:
    if czy_pierwsza4000(i):
        wynik.write(f"{i}\n")


wynik.close() #zamykam plik
