with open("input.txt", "r") as f:
    ids = f.readline()


ids = [[int(y) for y in x.split('-')] for x in ids.split(',')]
#ids = ids[:1]
score = 0

step = 0
for i in ids:
    step += 1
    print(step, len(ids))
    for number in range(i[0], i[1] + 1):
        s_number = str(number)
        for j in range(1, len(s_number)//2+1):
            t_number = s_number[:j]

            flag = 1

            for k in range(0, len(s_number), len(t_number)):
                #print(int(s_number[k:k+len(t_number)]), int(t_number))
                if int(s_number[k:k+len(t_number)]) != int(t_number):
                    flag = 0
                    break

            if flag:
                #print(t_number, number)
                score += number
                break

print(score)