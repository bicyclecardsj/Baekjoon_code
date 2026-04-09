N = int(input())
words = []
for _  in range(N):
    word = input()
    words.append(word)

uni_words = list(set(words))

sor_words = sorted(uni_words, key = lambda x:(len(x), x))

for w in sor_words:
    print(w)