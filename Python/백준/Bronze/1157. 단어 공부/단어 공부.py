import sys

word = sys.stdin.readline().strip().upper()

if not word:
    exit()

unique_words = list(set(word))
cnt_list = []

for x in unique_words:
    cnt = word.count(x)
    cnt_list.append(cnt)

max_cnt = max(cnt_list)

if cnt_list.count(max_cnt) > 1:
    print('?')
else:
    print(unique_words[cnt_list.index(max_cnt)])