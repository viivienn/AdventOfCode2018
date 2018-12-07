import itertools

file = [int(change) for change in open("input.txt").readlines()]

# CHALLENGE 1

print("Final frequency: " + str(sum(file)))

# CHALLENGE 2

allFreq = set()
frequency = 0

for change in itertools.cycle(file):
    frequency += change
    if frequency in allFreq:
        print("First repeated frequency: " + str(frequency));
        break
    else:
        allFreq.add(frequency)
