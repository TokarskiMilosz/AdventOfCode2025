with open("input.txt", "r") as f:
    ids = f.readline()


ids = [[int(y) for y in x.split('-')] for x in ids.split(',')]

score = 0
for i in ids:
    for number in range(i[0], i[1] + 1):
        temp = str(number)
        if len(temp) % 2 == 0:
            n1 = temp[:len(temp)//2]
            n2 = temp[len(temp)//2:]

            if int(n1) == int(n2):
                score += number

print(score)