T = int(input())

for _ in range(T):
    S = input().split()
    S_int = int(S[0])
    S_word = list(S[1])
    for i in S_word:
        print(i * S_int, end = '')
    print()