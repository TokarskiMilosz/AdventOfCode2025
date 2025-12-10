with open("input.txt", "r") as f:
    file = f.readlines()

file = [x.strip("\n").split() for x in file]

score = 0

for i in range(len(file[0])):
    numbers = int(file[0][i])
    for j in range(1, len(file) - 1):
        if file[-1][i] == '+':
            numbers += int(file[j][i])
        else:
            numbers *= int(file[j][i])
    score += numbers

print(score)