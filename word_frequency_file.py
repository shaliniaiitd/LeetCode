from collections import Counter


with open("words.txt", "r") as f:
    lines = f.readlines()

words = []
for line in lines:
    words_one_line = line.split(" ")

    words_one_line = list(map(str.lower, words_one_line))
    words_one_line = list(map(str.strip, words_one_line))

    words.extend(words_one_line)

count_dict = Counter(words)

#sort by values

sorted_count = dict(sorted(count_dict.items(), key = lambda x: x[1], reverse=True))

for key,value in sorted_count.items():
    print (key, value )