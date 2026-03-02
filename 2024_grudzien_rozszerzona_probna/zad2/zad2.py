def F(x,p):
    global counter
    counter += 1
    if x == 0:
        return 0
    else:
        c = x % p
        if c %2 ==1:
            return F(x//p, p) + c
        else:
            return F(x//p, p) - c

counter = 0
print(F(125,2), counter)
counter = 0
print(F(130,3), counter)
counter = 0
print(F(220,4), counter)