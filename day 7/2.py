with open("input.txt", "r") as f:
    file = f.readlines()

file = [list(x.strip("\n")) for x in file]

score_char = 0
for f in file:
    for c in f:
        if c == "^":
            score_char += 1

print(score_char)

beam = file[0].index("S")
beams = []
timeline_score = 1


def split_timeline(start_line, start_column):
    global file
    global timeline_score
    global beams

    for i in range(start_line, len(file[0]), 2):
        if file[i][start_column] == "^":
            if (start_line, start_column) not in beams:
                beams.append((start_line, start_column))
                print(len(beams), score_char)
            timeline_score += 1
            #print(start_line, start_column)
            split_timeline(i + 2, start_column + 1)
            split_timeline(i + 2, start_column - 1)
            break

split_timeline(2, beam)
print(timeline_score)