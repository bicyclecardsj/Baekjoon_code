score_list = []
for i in range(8):
    score = int(input())
    score_list.append((score, i + 1))

score_list.sort(key=lambda x: x[0], reverse=True)

score_sum = 0
top_indices = []

for j in range(5):
    score_sum += score_list[j][0]
    top_indices.append(score_list[j][1]) 

print(score_sum)

top_indices.sort()
print(*(top_indices))