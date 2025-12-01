with open("input.txt", "r") as f:
    instructions = f.readlines()

instructions = [x.strip() for x in instructions]

dial = 50

score = 0

for i in instructions:

    if i[0] == "R":
        dial += int(i[1:]) % 100
    elif i[0] == "L":
        dial -= int(i[1:]) % 100

    if dial > 99:
        dial -= 100
    elif dial < 0:
        dial += 100

    if dial == 0:
        score += 1

print(score)