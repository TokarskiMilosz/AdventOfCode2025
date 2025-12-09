from functools import lru_cache

with open("input.txt", "r") as f:
    file = f.readlines()

file = [list(x.strip("\n")) for x in file]


splits = []

for i in range(2, len(file), 2):
    for j in range(len(file[0])):
        if file[i][j] == "^":
            splits.append((i, j))

beams_graph = {(0, file[0].index("S")): [splits[0]]}

for i, split in enumerate(splits):
    beams_graph[split] = []

    for j in range(i + 1, len(splits)):
        if splits[j][1] - split[1] == -1:
            beams_graph[split].append(splits[j])
            break
    for j in range(i + 1, len(splits)):
        if splits[j][1] - split[1] == 1:
            beams_graph[split].append(splits[j])
            break

checked = []
#score = 1

print(beams_graph)

# @lru_cache(None)
# def timelines(start):
#     global beams_graph
#     global score
#
#     if len(beams_graph[start]) == 2:
#         score += 2
#         timelines(beams_graph[start][0])
#         timelines(beams_graph[start][1])
#     elif len(beams_graph[start]) == 1:
#         score += 1
#         timelines(beams_graph[start][0])
#
# timelines((0, file[0].index("S")))
#
# print(score)

@lru_cache(None)
def timelines(start):
    if len(beams_graph[start]) == 2:
        return 2 + timelines(beams_graph[start][0]) + timelines(beams_graph[start][1])
    elif len(beams_graph[start]) == 1:
        return 1 + timelines(beams_graph[start][0])
    else:
        return 0

score = timelines((0, file[0].index("S"))) + 1
print(score)

