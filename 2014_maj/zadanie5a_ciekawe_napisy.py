def is_prime(number):
    s = int(number ** (1 / 2)) + 1
    if number < 2:
        return False
    if number == 2 or number % 2 == 0:
        return False
    for i in range(3, s + 1, 2):
        if number % i == 0:
            return False
    return True


def to_ascii_sum(word):
    ascii_sum = 0
    for w in word:
        ascii_sum += ord(w)
    return ascii_sum


# print(is_prime(100000007))
# print(is_prime(12))
a = to_ascii_sum("ABB")
print(a)
print(is_prime(a))
counter = 0

with open("NAPIS.TXT", 'r') as file:
    words = file.read().split()

for w in words:
    a = to_ascii_sum(w)
    if is_prime(a):
        counter += 1
print(counter)
