with open("input.txt", "r") as f:
    banks = f.readlines()

banks = [x.strip("\n") for x in banks]

score = 0
for bank in banks:
    score += int(max(bank[:-1]) + max(bank[bank.index(max(bank[:-1])) + 1:]))

print(score)