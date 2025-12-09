with open("input.exe", "r") as f:
    file = f.readlines()

file = [x.strip("\n") for x in file]

ranges = [list(map(int, x.split("-"))) for x in file if "-" in x and x != ""]

ids = [int(x) for x in file if "-" not in x and x != ""]


temp_ranges = {}
for r in ranges:
    if r[0] not in temp_ranges:
        temp_ranges[r[0]] = []
        temp_ranges[r[0]].append(r[1])
    else:
        temp_ranges[r[0]].append(r[1])

print(temp_ranges)

ranges = [[x, max(temp_ranges[x])] for x in temp_ranges]

print(ranges)

ranges.sort()
print(ranges)

new_ranges = [ranges[0]]

for i, r in enumerate(ranges):
    print(r)
    if new_ranges[-1][1] < r[0]:
        new_ranges.append(r)
    elif r[0] <= new_ranges[-1][1] and r[1] > new_ranges[-1][1]:
        new_ranges[-1] = [new_ranges[-1][0], r[1]]
    print(new_ranges, "\n")


print(new_ranges)

score = 0
for r in new_ranges:
    score += r[1] - r[0] + 1

print(score)




