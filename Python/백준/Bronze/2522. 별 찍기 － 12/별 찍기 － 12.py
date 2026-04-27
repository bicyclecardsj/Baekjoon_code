N = int(input())
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)
for j in range(2, N + 1):
    print(' ' * (j - 1) + '*' * ((N + 1) - j))