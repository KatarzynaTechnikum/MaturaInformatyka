

def nwd(a, b):
    while b:
        return nwd(b, a % b)
    return a

def pwp(a):
    a_copy = a
    digit_number = 0
    divisor = 1
    while a > 0:
        digit_number += 1
        a //= 10

    for i in range(digit_number//2):
        divisor *= 10
    a = a_copy // divisor
    b = a_copy % divisor
    # print(a, b)
    return nwd(a, b) == 1


path = "liczby1.txt"
# path = "liczby1_przyklad.txt"
with open(path, "r") as file:
    numbers = list(map(int, file.read().split())) #file.readlines()
print(numbers)
counter = 0
for number in numbers:
    if pwp(number):
        counter += 1
with open("wyniki2_2.txt", "w") as file:
    file.write(str(counter))





