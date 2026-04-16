A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
list_mul = list(str(mul))

for i in range(10):
    print(list_mul.count(str(i)))