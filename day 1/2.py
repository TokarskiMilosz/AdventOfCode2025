with open("input.txt", "r") as f:
    instructions = f.readlines()

instructions = [x.strip() for x in instructions]

dial = 50

score = 0

for i in instructions:
    if i[0] == "R":
        turn = 1
    else:
        turn = -1

    for j in range(int(i[1:])):
        dial += turn

        if dial == 100:
            dial = 0
        elif dial == -1:
            dial = 99

        if dial == 0:
            score += 1

print(score)




