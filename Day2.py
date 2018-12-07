from collections import Counter

lines = open("input2.txt").read().splitlines()

# CHALLENGE 1

counter = Counter()

for char in lines:
    counter.update(set(Counter(char).values()))

print("CHECKSUM: " + str(counter[2] * counter[3]))

#CHALLENGE 2


from itertools import combinations

for (x, y) in combinations(lines, 2):
    difference = [a == b for (a, b) in zip(x, y)]
    if sum(difference) == len(x) - 1:
        word = ''.join([x[i] for i in range(len(x)) if i != difference.index(False)])
        print("Common letter: " + word)
