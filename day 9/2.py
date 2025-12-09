with open("input.txt", "r") as f:
    file = f.readlines()

tiles = [[int(x) for x in y.strip("\n").split(",")] for y in file]

max_x = max(x[0] for x in tiles)
max_y = max(x[1] for x in tiles)


#znalezc poczatek i szukac jak zegar i laczyc w area i tabela connect
def first_search(tiles):
    min_y = min(x[1] for x in tiles)
    min_row = [x for x in tiles if x[1] == min_y]
    min_x =  min(x[0] for x in min_row)

    return [min_x, min_y]

def up(tiles, xs, ys):
    same_x = [x for x in tiles if x[0] == xs]
    up_y = [x for x in same_x if x[1] < ys]
    if len(up_y):
        max_y = max(x[1] for x in up_y)
        return [xs, max_y]
    return 0

def right(tiles, xs, ys):
    same_y = [x for x in tiles if x[1] == ys]
    right_x = [x for x in same_y if x[0] > xs]
    if len(right_x):
        min_x = min(x[0] for x in right_x)
        return [min_x, ys]
    return 0

def left(tiles, xs, ys):
    same_y = [x for x in tiles if x[1] == ys]
    left_x = [x for x in same_y if x[0] < xs]
    if len(left_x):
        max_x = max(x[0] for x in left_x)
        return [max_x, ys]
    return 0

def down(tiles, xs, ys):
    same_x = [x for x in tiles if x[0] == xs]
    down_y = [x for x in same_x if x[1] > ys]
    if len(down_y):
        min_y = min(x[1] for x in down_y)
        return [xs, min_y]
    return 0

#area = [['.' for x in range(max_x+5)] for y in range(max_y+5)]
# for tile in tiles:
#     area[tile[1]][tile[0]] = "#"
# for a in area:
#     print("".join(a))

#ruch wskzówek zegara obliczanie tego najwiekszego

can_connect = 1
tile = first_search(tiles)

tile_connections = {(x[0], x[1]): 0 for x in tiles}

while can_connect:
    tile_up = up(tiles, tile[0], tile[1])
    tile_right = right(tiles, tile[0], tile[1])
    tile_down = down(tiles, tile[0], tile[1])
    tile_left = left(tiles, tile[0], tile[1])

    if tile_up and tile_connections[(tile_up[0], tile_up[1])] < 2:
        #print("up")
        tile_connections[(tile[0], tile[1])] += 1
        tile_connections[(tile_up[0], tile_up[1])] += 1
        tile = tile_up

    elif tile_right and tile_connections[(tile_right[0], tile_right[1])] < 2:
        #print("right")
        tile_connections[(tile[0], tile[1])] += 1
        tile_connections[(tile_right[0], tile_right[1])] += 1
        tile = tile_right

    elif tile_down and tile_connections[(tile_down[0], tile_down[1])] < 2:
        #print("down")
        tile_connections[(tile[0], tile[1])] += 1
        tile_connections[(tile_down[0], tile_down[1])] += 1
        tile = tile_down

    elif tile_left and tile_connections[(tile_left[0], tile_left[1])] < 2:
        #print("left")
        tile_connections[(tile[0], tile[1])] += 1
        tile_connections[(tile_left[0], tile_left[1])] += 1
        tile = tile_left

    else:
        can_connect = 0



