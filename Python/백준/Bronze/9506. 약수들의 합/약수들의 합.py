while True:
    n = int(input())
    if n == -1:
        break
    div_list = []
    for i in range(1, n):
        if n % i == 0:
            div_list.append(i)
    
    if sum(div_list) == n:
        result = ' + '.join(map(str, div_list))
        print(f'{n} = {result}')
    else:
        print(f'{n} is NOT perfect.')