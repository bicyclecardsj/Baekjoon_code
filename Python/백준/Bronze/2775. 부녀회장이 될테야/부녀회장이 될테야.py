T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    row = []
    for i in range(1, n+1):
        row.append(i)
    for c in range(k):
        for r in range(1, n):
            row[r] += row[r - 1]
    print(row[n - 1])