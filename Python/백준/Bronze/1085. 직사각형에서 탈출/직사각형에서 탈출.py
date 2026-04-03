x, y, w, h = map(int, input().split())
min_x = 0
min_y = 0
if w / 2 < x:
    min_x = w - x
else:
    min_x = x

if h / 2 < y:
    min_y = h - y
else:
    min_y = y

print(min(min_x, min_y))