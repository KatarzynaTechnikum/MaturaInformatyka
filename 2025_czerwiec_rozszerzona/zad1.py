c = 0
cw = 0
def f(a, b):
    global c
    global cw
    c += 1
    if b == 0:
        return 0
    k = b % 10
    w = f(a, b // 10)
    w *= 10
    while k > 0:
        w += a
        cw += 1
        k -= 1
    return w

#zadanie 1.1
print(f(42, 2))
print(f(4, 125))
print(f(103, 104))
#zadanie 1.2
c = 0
print(f(987654321, 123456789))
print(c)


#zadanie 1.3
cw = 0
f(2024, 1000)
print(cw)
cw = 0
f(2024, 1234)
print(cw)