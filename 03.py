n = int(input())

i = 0

while True:
    if (1 << i) >= n:
        print(i)
        break
    i += 1
