data = map(int, input().split())
s = 0

for x in data:
    s += x
    if x == 0:
        break

print(s)

