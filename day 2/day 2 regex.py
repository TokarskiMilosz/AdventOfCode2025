import re

with open("example_input.txt", "r") as f:
    ids = f.readline()


ids = [[int(y) for y in x.split('-')] for x in ids.split(',')]
#ids = ids[:1]
score = 0

step = 0
for i in ids:
    step += 1
    for number in range(i[0], i[1] + 1):
        numbers = re.fullmatch(r"(.+)\1+", str(number))
        print(bool(numbers))
