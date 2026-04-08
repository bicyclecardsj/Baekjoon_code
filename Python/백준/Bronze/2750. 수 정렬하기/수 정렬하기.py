N = int(input())
asce_list = []
for i in range(N):
    num = int(input())
    asce_list.append(num)
list = sorted(asce_list)
print("\n".join(map(str, list)))