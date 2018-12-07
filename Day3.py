import numpy as np
import parse

SIZE = 1000

claim = [open("input3.txt").read().splitlines()]

claim_matcher = '''#{id:d} @ {x:d},{y:d}: {width:d}x{height:d}\n'''
fabric = np.zeros((1000, 1000), dtype=np.int)

print(claim_matcher)
print(fabric)