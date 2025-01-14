import random

print("Minefield:")

w = 20
h = 5
mine_cnt = 10


# vygeneruje pole
field = [[0 for i in range(h)] for j in range(w)]


# položí minu na náhodnou pozici
if mine_cnt > w * h:
    mine_cnt = 0
    print("Too many mines.")
for i in range(mine_cnt):
    while True:
        rx = random.randint(0, w - 1)
        ry = random.randint(0, h - 1)
        if field[rx][ry] != "M":
            field[rx][ry] = "M"
            break

# ověří kde leží mina
deltas = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
for y in range(h):
    for x in range(w):
        if field[x][y] == "M":
            for delta in deltas:
                nx = x + delta[0]
                ny = y + delta[1]
                if nx >= 0 and nx < w and ny >= 0 and ny < h and field[nx][ny] != "M":
                    field[nx][ny] += 1

# tisk pole
for y in range(h):
    for x in range(w):
        print(field[x][y], sep="", end="")
    print()