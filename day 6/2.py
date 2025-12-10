with open("input.txt", "r") as f:
    file = f.readlines()

file = [x.strip("\n") for x in file]

symbol_index = [i for i in range(0, len(file[-1])) if file[-1][i] in "+*"]

numbers = [[] for x in symbol_index]

for i in range(0, len(symbol_index) - 1):
    for j in range(len(file)):
        numbers[i].append(file[j][symbol_index[i]:symbol_index[i + 1]-1])

for j in range(len(file)):
    numbers[-1].append(file[j][symbol_index[-1]:len(file[j])])

for i in range(len(numbers[-1])):
    if len(numbers[-1][i]) < len(max(numbers[-1], key=len)):
        numbers[-1][i] += " " * (len(max(numbers[-1], key=len)) - len(numbers[-1][i]))

score = 0
for n in numbers:
    temp_numbers = []
    for i in range(len(n[0])):
        temp_number = ""
        for j in range(len(n) - 1):
            temp_number += n[j][i]
        temp_numbers.append(int(temp_number))


    if '*' in n[-1]:
        temp_score = 1
        for x in temp_numbers:
            temp_score *= x
        score += temp_score
    else:
        score += sum(temp_numbers)

print(score)


