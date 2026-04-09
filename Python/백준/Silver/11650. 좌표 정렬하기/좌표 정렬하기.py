N = int(input())
points = []

for _ in range(N):
    point = list(map(int, input().split()))
    points.append(point)

points.sort()

for p in points:
    print(f'{p[0]} {p[1]}')