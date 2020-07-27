'''
sequence = [int(x) for x in input()]
for i in range(1, len(sequence)):
    sequence[i] += sequence[i-1]
print(sequence)
'''

text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

length_words = int(input())

for lists in text:
    for words in lists:
        if len(words) <= length_words:
            print(words)

print([words for lists in text for words in lists if len(words) <= length_words])
