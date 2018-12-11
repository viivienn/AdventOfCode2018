import numpy as np
import parse

fab = np.zeros((1000, 1000))
pattern = '''#{id:d} @ {fromLeft:d},{fromTop:d}: {width:d}x{height:d}\n'''

# PART 1

for line in open("input_d3.txt"):
    claim = parse.parse(pattern, line)
    fab[claim['fromLeft']:claim['fromLeft'] + claim['width'], claim['fromTop']:claim['fromTop'] + claim['height']] += 1

print("Number of squares: " + str(np.sum(fab >= 2)))

# PART 2

for line in open("input_d3.txt"):
    claim = parse.parse(pattern, line)
    if(np.all(fab[claim['fromLeft']:claim['fromLeft'] + claim['width'], claim['fromTop']:claim['fromTop'] + claim['height']] == 1)):
        print("ID: " + str(claim['id']))
