with open("input.exe", "r") as f:
    area = f.readlines()


area = [x.strip("\n") for x in area]

score = 0

for row in range(len(area)):
    for column in range(len(area[0])):
        if area[row][column] == "@":
            flag = 1
            paper = 0
            for x in range(-1, 2):
                if flag == 0:
                    break
                for y in range(-1, 2):

                    if x == 0 and y == 0:
                        continue
                    elif row == 0:
                        if column == 0 and (x == -1 or y == -1):
                            continue
                        if column == len(area[0]) -1 and (x == 1 or y == -1):
                            continue
                        if y == -1:
                            continue
                    elif row == len(area) - 1:
                        if column == 0 and (x == -1 or y == 1):
                            continue
                        if column == len(area[0]) -1 and (x == 1 or y == 1):
                            continue
                        if y == 1:
                            continue
                    elif column == 0 and x == -1:
                        continue
                    elif column == len(area[0]) - 1 and x == 1:
                        continue
                    #print(row, y, column, x)
                    if area[row + y][column + x] == "@":
                        paper += 1
                        if paper == 4:
                            flag = 0
                            break
            if flag:
                #print("->", row, column)
                score += 1


print(score)



