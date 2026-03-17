isbn = input()
total = 0
idx = isbn.index("*")

for i in range(len(isbn)):
    if i == idx:
        continue
    if i % 2 == 0:
        total += int(isbn[i])
    else:
        total += int(isbn[i]) * 3

for n in range(10):
    weight = 1 if idx % 2 == 0 else 3
    if (total + n * weight) % 10 == 0:
        print(n)
        break