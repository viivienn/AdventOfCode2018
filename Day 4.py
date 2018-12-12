from collections import Counter, defaultdict

file = sorted(open("input_d4.txt").readlines())

journal = defaultdict(Counter)

# Parsing & writing the journal using string splitting
# Journal updates with Counter

for line in file:
    min = int(line.split()[1][3:5])
    if 'Guard' in line:
        guard = int(line.split('#')[1].split()[0])
    if 'sleep' in line:
        start = min
    if 'wakes' in line:
        journal[guard].update([i for i in range(start, min)])

# Challenge 1

naptime = 0
for id, time in journal.items():
    if sum(time.values()) > naptime:
        naptime = sum(time.values())
        lazyGuard = id

print("Laziest guard * snoozy minute = " + str(lazyGuard * journal[lazyGuard].most_common()[0][0]))

# Challenge 2

sleepiestMinute = 0
freq = 0
for id, time in journal.items():
    if time.most_common()[0][1] > freq:
        lazyGuard = id
        sleepiestMinute = time.most_common()[0][0]
        freq = time.most_common()[0][1]

print("Sleepiest guard * sleepy minute = " + str(lazyGuard * sleepiestMinute))
