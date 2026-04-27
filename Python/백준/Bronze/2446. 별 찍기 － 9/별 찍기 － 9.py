N = int(input())
for i in range(1, N + 1):
    print(' ' * (i - 1) + '*' * ((N + 1) - i) + '*' * (N - i))
for j in range(2, N + 1):
    print(' ' * (N - j) + '*' * j + '*' * (j - 1))