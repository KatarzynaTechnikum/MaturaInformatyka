def stopienKaprekara(n):
    original_n = n
    n *= n
    n_copy = n

    d = 1
    s = 0
    while n  >  0:
        # print(n)
        d *= 10
        a = n_copy //d
        b = n_copy % d
        # print(a, b)
        n //= 10
        # print(n)
        # print(a+b)
        if a + b <= original_n:
            s += 1
    return s

# print(stopienKaprekara(2757))
# print(stopienKaprekara(89))

path = "liczby2.txt"
# path = "liczby2_przyklad.txt"
with open(path, "r") as file:
    numbers = list(map(int, file.read().split())) #file.readlines()
# print(numbers)
counter = 0


list_numbers = []
max_st = 0
for number in numbers:
    st = stopienKaprekara(number)
    if st > max_st:
        max_st = st
        list_numbers.clear()
        list_numbers.append(number)
    elif st == max_st:
        list_numbers.append(number)
print(max_st)
print(*list_numbers)