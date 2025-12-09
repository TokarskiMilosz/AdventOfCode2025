with open("input.txt", "r") as f:
    file = f.readlines()

tiles = [[int(x) for x in y.strip("\n").split(",")] for y in file]

largest = 0

for i, tile1 in enumerate(tiles):
    for j in range(i + 1, len(tiles)):
        tile2 = tiles[j]
        area = (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)

        if area > largest:
            largest = area

print(largest)
