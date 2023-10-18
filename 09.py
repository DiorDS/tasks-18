from datetime import date


d, m, y = map(int, input().split())
d2, m2, y2 = map(int, input().split())

print((date(y2, m2, d2) - date(y, m, d)).days)

