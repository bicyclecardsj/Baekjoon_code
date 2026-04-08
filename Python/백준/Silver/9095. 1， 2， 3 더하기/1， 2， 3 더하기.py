T = int(input())
for _ in range(T):
    n = int(input())
    tab = [0, 1, 2, 4] + [0] * (n - 3)
    for i in range(4, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2] + tab[i - 3]
    print(tab[n])