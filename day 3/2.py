with open("input.txt", "r") as f:
    banks = f.readlines()

banks = [x.strip("\n") for x in banks]

lenght = len(banks[0])
score = 0
#banks = banks[2:3]

for bank in banks:
    joltage = max(bank[:-11])
    current_index = bank.index(joltage) + 1

    for i in range(10):
        end = -11 + len(joltage)
        #print(current_index, -11+len(joltage), bank[current_index:end], bank)


        joltage += max(bank[current_index:end])
        current_index += bank[current_index:end].index(max(bank[current_index:end])) + 1
        #print(joltage, current_index)

    joltage += max(bank[current_index:])
    #print(joltage)

    score += int(joltage)

print(score)

