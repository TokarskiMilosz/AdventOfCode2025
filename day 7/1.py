with open("input.txt", "r") as f:
    file = f.readlines()

file = [list(x.strip("\n")) for x in file]

beams = set()
beams.add(file[0].index("S"))

split_score = 0

for i, line in enumerate(file, start=2):
    for j, point in enumerate(line):
        if point == '^' and j in beams:
            split_score += 1
            beams.remove(j)
            beams.add(j-1)
            beams.add(j+1)

print(split_score)