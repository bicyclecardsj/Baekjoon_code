while True:
    line = input()
    if line == '#':
        break
    sen = list(line.upper())
    count = 0
    for i in sen:
        if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            count += 1
    print(count)