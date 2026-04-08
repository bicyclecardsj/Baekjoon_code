N = int(input())
result = 0
for i in range(1, N + 1):
    list_N = list(map(int, str(i)))
    sum_N = sum(list_N) + i

    if sum_N == N:
        result = i
        break
print(result)