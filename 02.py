n = int(input())

i = 0

while (1 << i) <= n:
    print(1 << i)
    i += 1
