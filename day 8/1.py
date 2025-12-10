from math import sqrt
from collections import defaultdict

with open("input.txt", "r") as f:
    file = f.readlines()

cordinates = [[int(y) for y in x.strip("\n").split(",")] for x in file]

#j1, j2, distance
junction_boxes_distance = {}

for i, cordinate in enumerate(cordinates):
    for j in range(i + 1, len(cordinates)):
        junction_boxes_distance[(i, j)] = sqrt(pow((cordinate[0] - cordinates[j][0]), 2) + pow((cordinate[1] - cordinates[j][1]), 2) + pow((cordinate[2] - cordinates[j][2]), 2))

connections = 1000

sorted_junction_boxes_distance = dict(sorted(junction_boxes_distance.items(), key=lambda x: x[1]))

circuits = []

circuits_index = {}

for junction_boxes in sorted_junction_boxes_distance:
    if not connections:
        break

    if junction_boxes[0] not in circuits_index and junction_boxes[1] not in circuits_index:
        circuits_index[junction_boxes[0]] = len(circuits)
        circuits_index[junction_boxes[1]] = len(circuits)
        circuits.append([junction_boxes[0], junction_boxes[1]])

    elif junction_boxes[0] not in circuits_index and junction_boxes[1] in circuits_index:
        circuits_index[junction_boxes[0]] = circuits_index[junction_boxes[1]]
        circuits[circuits_index[junction_boxes[1]]].append(junction_boxes[0])

    elif junction_boxes[1] not in circuits_index and junction_boxes[0] in circuits_index:
        circuits_index[junction_boxes[1]] = circuits_index[junction_boxes[0]]
        circuits[circuits_index[junction_boxes[0]]].append(junction_boxes[1])

    elif circuits_index[junction_boxes[0]] != circuits_index[junction_boxes[1]]:
        circuits[circuits_index[junction_boxes[0]]] += circuits[circuits_index[junction_boxes[1]]]

        for c in circuits[circuits_index[junction_boxes[1]]]:
            circuits_index[c] = circuits_index[junction_boxes[0]]

        circuits_index[junction_boxes[1]] = circuits_index[junction_boxes[0]]

    connections -= 1

sorted_circuits = sorted(circuits, key=len, reverse=True)

score = len(sorted_circuits[0]) * len(sorted_circuits[1]) * len(sorted_circuits[2])

print(score)