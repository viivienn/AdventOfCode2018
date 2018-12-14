from collections import Counter

coord = [list(map(int, x.split(', '))) for x in open("input_d6.txt").readlines()]

x_min = min(coord, key=lambda k: k[0])[0]
x_max = max(coord, key=lambda k: k[0])[0]
y_min = min(coord, key=lambda k: k[1])[1]
y_max = max(coord, key=lambda k: k[1])[1]


def man_distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def is_finite(x, y):
    return x_min < x < x_max and y_min < y < y_max


def equal_distance(dist):
    return sorted(dist)[0] == sorted(dist)[1]


area = Counter()
infinite_coord = set()
region = 0

for x in range(x_min, x_max):
    for y in range(y_min, y_max):
        dist = [man_distance([x, y], i) for i in coord]

        closest = dist.index(min(dist))

        if not is_finite(x, y) and closest not in infinite_coord:
            infinite_coord.add(closest)

        if not equal_distance(dist) and closest not in infinite_coord:
            area[closest] += 1

        # Part 2 - everything above is Part 1
        if sum(dist) < 10000:
            region += 1

print("Largest area: " + str(max(area.values())))

print("Region size: " + str(region))
