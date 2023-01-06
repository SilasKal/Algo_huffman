import heapq

word = input()
H = []

if len(word) == 1:
    print('1')
else:
    for i in word:
        if i not in count_list:
            count_list.append(i)

dict_word_count = {i:word.count(i) for i in word}
H = [[i, [letter, 0]] for letter, i in dict_word_count.items()]
heapq.heapify(H)
while len(H) > 1:
    right_child = heapq.heappop(H)
    left_child = heapq.heappop(H)
    for i in right_child[1:]:
        i[1] += 1
    for i in left_child[1:]:
        i[1] += 1
    heapq.heappush(H, [right_child[0] + left_child[0]] + right_child[1:] + left_child[1:])

dict_2 = {i[0]:i[1] for i in right_child[1:]+left_child[1:]}

summe = 0

for i in dict_2.keys():
    summe += dict_2[i] * dict_word_count[i]
print(summe)
