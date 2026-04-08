def fib_mem(num):
    if mem[num] == -1:
        mem[num] = fib_mem(num-1) + fib_mem(num-2)
    return mem[num]

n = int(input())
mem = [0, 1] + [-1] * (n - 1)
print(fib_mem(n))