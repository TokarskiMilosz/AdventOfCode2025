with open("input.exe", "r") as f:
    file = f.readlines()

file = [x.strip("\n") for x in file]

ranges = [list(map(int, x.split("-"))) for x in file if "-" in x and x != ""]

ids = [int(x) for x in file if "-" not in x and x != ""]

score = 0

x = 0
for i in ids:
    x += 1
    print(x, len(ids))
    flag = 0
    for r in ranges:
        if r[0] <= i <= r[1]:
            flag = 1
            break
    if flag:
        score += 1

print(score)