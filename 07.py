data = map(int, input().split())

f = False
s = 0

for x in data:
    s += x
    if not f and x == 0:
        f = True
    elif f and x == 0:
        break
    else:
        f = False

print(s)
