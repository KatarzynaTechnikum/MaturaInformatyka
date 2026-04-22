with open("NAPIS.TXT", 'r') as file:
    words = file.read().split()

f = []
for w in words:
    if words.count(w) > 1 and w not in f:
        f.append(w)

for i in f:
    print(i)
