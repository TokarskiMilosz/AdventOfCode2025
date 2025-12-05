with open("example_input.exe", "r") as f:
    file = f.readlines()

file = [x.strip("\n") for x in file]

ranges = [list(map(int, x.split("-"))) for x in file if "-" in x and x != ""]

ids = [int(x) for x in file if "-" not in x and x != ""]

score = 0

fresh = set()

x = 0
def sum_inside(ranges, new_ranges_number = 1):
    if new_ranges_number > 0:
        new_ranges_number = 0
        range_to_delete = []
        for i, range_bigger in enumerate(ranges):
            for j in range(0, len(ranges)):
                if range_bigger[0] <= ranges[j][0] and range_bigger[1] >= ranges[j][1] and i != j:
                    #print(range_bigger, ranges[j])
                    range_to_delete.append(ranges[j])
                    new_ranges_number += 1
        ranges = [x for x in ranges if x not in range_to_delete]
        sum_inside(ranges, new_ranges_number)
    return ranges

def sum_outside(ranges, new_ranges_number = 1):
    if new_ranges_number > 0:
        new_ranges_number = 0
        new_ranges = []

        for i, range1 in enumerate(ranges):
            flag = 1
            for j in range(0, len(ranges)):
                range2 = ranges[j]

                if range1[1] >= range2[0] and range2[1] > range1[0] and i != j:
                    print(range1, range2)
                    new_ranges.append([range1[0], range2[1]])
                    print(new_ranges)
                    new_ranges_number += 1
                    flag = 0
                    break
                elif range1[0] <= range2[1] and range1[1] > range2[0] and i != j:
                    print(range1, range2)
                    new_ranges.append([range2[0], range1[1]])
                    print(new_ranges)
                    new_ranges_number += 1
                    flag = 0
                    break
            if flag:
                new_ranges.append(range1)
        print(new_ranges)
        return
        sum_outside(new_ranges, new_ranges_number)
    return new_ranges

print(sum_outside(ranges))
