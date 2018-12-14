from collections import Counter

coord = [list(map(int, x.split(', '))) for x in open("input_d6.txt").readlines()]

x_min = min(coord, key=lambda k: k[0])[0]
x_max = max(coord, key=lambda k: k[0])[0]
y_min = min(coord, key=lambda k: k[1])[1]
y_max = max(coord, key=lambda k: k[1])[1]

def man_distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def is_finite(x,y):
    return x_min < x < x_max and y_min < y < y_max

def equal_distance(dist):
    return sorted(dist)[0] == sorted(dist)[1]

area = Counter()
infinite_coord = set()

def part_1():
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            dist=[man_distance([x, y], i) for i in coord]

            closest = dist.index(min(dist))

            if not is_finite(x, y) and closest not in infinite_coord:
                infinite_coord.add(closest)

            if not equal_distance(dist) and closest not in infinite_coord:
                    area[closest] += 1
    return max(area.values())

print(part_1())











'''


def calculate_counts(bound):
    region = 0
    counts = defaultdict(lambda: 0)
    grid = [['.' for x in range(min_ x -bound, max_ x +bound)] for y in range(min_ y -bound, max_ y +bound) ]
    for row in range(min_ y -bound, max_ y +bound):
        for col in range(min_ x -bound, max_ x +bound):
            distances = {}
            for i in range(len(coords)):
                distances[i] = manhattan_distance([col, row], coords[i])
            if sum(distances.values()) < 10000:
                region += 1
            closest_val = min(distances.values())

            closest_coord = [k for k, v in distances.items() if v == closest_val]

            if len(closest_coord) == 1:
                grid[(ro w -min_y ) -bound][(co l -min_x ) -bound] = closest_coord[0]
                counts[closest_coord[0]] += 1
    return counts, region

counts1, _ = calculate_counts(10)
counts2, region = calculate_counts(20)

finite_counts = []
for k, v in counts1.items():
    if counts2[k] == v:
        finite_counts.append(v)

print("Largest Finite Area(pt1): {area}, Region(pt2): {region}".format(area=max(finite_counts), region=region))
'''
'''
#_______________________________
from collections import Counter

data = [map(int, i.split(', ')) for i in open('../input/6.in').readlines()]

max_x = max(zip(*data)[0])
max_y = max(zip(*data)[1])
grid={}
for i in range(max_x):
    for j in range(max_y):
        m = min(abs(i-k)+abs(j-l) for k, l in data)
        for n, (k, l) in enumerate(data):
            if abs(i-k)+abs(j-l) == m:
                if grid.get((i, j), -1) != -1:
                    grid[i, j] = -1
                    break
                grid[i, j] = n

s = set([-1])
s = s.union(set(grid[x, max_y-1] for x in range(max_x)))
s = s.union(set(grid[x,       0] for x in range(max_x)))
s = s.union(set(grid[max_x-1, y] for y in range(max_y)))
s = s.union(set(grid[      0, y] for y in range(max_y)))

print next(i[1] for i in Counter(grid.values()).most_common() if i[0] not in s)
print sum(sum(abs(i-k)+abs(j-l) for k, l in data) < 10000 for i in range(max(zip(*data)[0]))
                                                          for j in range(max(zip(*data)[1])))
#---------------------------------
from util import get_data
import re
from collections import defaultdict
d = get_data(6)


d = map(lambda s: map(int, re.findall(r'-?\d+', s)), d)
min_x = min(x[0] for x in d)-(10000/len(d))-1
max_x = max(x[0] for x in d)+(10000/len(d))+1
min_y = min(x[1] for x in d)-(10000/len(d))-1
max_y = max(x[1] for x in d)+(10000/len(d))+1
mapping = {}
in_region = set()
for x in xrange(min_x, max_x+1):
  for y in xrange(min_y, max_y+1):
    closest = d[0]
    closest_dist = (1 << 31)
    dist_sum = 0
    for (px, py) in d:
      dist = abs(px - x) + abs(py - y)
      dist_sum += dist
      if dist < closest_dist:
        closest = (px, py)
        closest_dist = dist
      elif dist == closest_dist and closest != (px, py):
        closest = None
    mapping[(x, y)] = closest
    if dist_sum < 10000:
      in_region.add((x, y))

rev_mapping = defaultdict(int)
for h in mapping:
  if not mapping[h]:
    continue
  if h[0] in (min_x, max_x) or h[1] in (min_y, max_y):
    rev_mapping[mapping[h]] -= (1 << 31)
  rev_mapping[mapping[h]] += 1
print "a", max(rev_mapping.values())
print "b", len(in_region)
#----------------------------
'''