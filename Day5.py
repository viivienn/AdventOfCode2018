from functools import reduce

file = open("input_d5.txt").read()

# Challenge 1

def sameLetter(x, y):
    if 1 > len(x):
        return False
    elif x[-1].lower() == y.lower() and x[-1] != y:
        return True

def reduction(x, y):
    if sameLetter(x, y):
        return x[:-1]
    else:
        return x + y

print(len(reduce(reduction, file)))

# Challenge 2
# Ugly one-liner self-challenge also!

print(min(len(reduce(reduction, file.replace(chr(ord('a') + i), '').replace(chr(ord('A') + i), ''))) for i in range(0, 26)))

