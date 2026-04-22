def growing_string(w):
    for i in range(1, len(w)):
        if ord(w[i - 1]) >= ord(w[i]):
            return False
    return True


with open("NAPIS.TXT", 'r') as file:
    words = file.read().split()

for w in words:
    if growing_string(w):
        print(w)
