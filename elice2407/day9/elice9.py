# import pdb

N = int(input())
Map = []
for _ in range(N):
    row = list(map(int,input().split()))
    Map.append(row)
elice_pos = []
# elice_str = [['.']*N for _ in range(N)]
# elice_char = ['E', 'L', 'I', 'C', 'E']
for i in range(5):
    row = tuple(map(int,input().split()))
    row = (row[1]-1, row[0]-1)
    elice_pos.append(row)
    # elice_str[row[1]][row[0]] = elice_char[i]
e1_pos, l_pos, i_pos, c_pos, e2_pos = elice_pos
# print("\n".join(["".join(row) for row in elice_str]))
# pdb.set_trace()


class Cell:
    def __init__(self, x, y):
        self.xy = (x,y)
        self.parent = (-1,-1)
        self.f = 0
        self.g = 0
        self.h = 0
    def __str__(self):
        return f"Cell{{xy:{self.xy}, parent:{self.parent}, f:{self.f}, g:{self.g}, h:{self.h}}}"
    def __repr__(self):
        return str(self)

def find_path(start, target):
    closed_cell = [[0] * N for _ in range(N)]
    open_cell = []
    cells = [[Cell(x,y) for x in range(N)] for y in range(N)]
    
    sx, sy = start
    open_cell.append(cells[sy][sx])
    directions = [(-1,0), (1,0), (0,-1), (0,1)] # L, R, U, D
    result_path = []
    result_dist = -1
    # print(open_cell)
    # pdb.set_trace()
    while len(open_cell) > 0:
        curr_cell = open_cell[0]
        cx, cy = curr_cell.xy
        closed_cell[cy][cx] = 1
        open_cell = open_cell[1:]
        # pdb.set_trace()
        if (cx,cy) == target:
            result_dist = curr_cell.f
            result_path = [(cx,cy)]
            px, py = curr_cell.parent
            while px != -1: # py != -1
                result_path.append((px,py))
                px, py = cells[py][px].parent
            # pdb.set_trace()
            break
        
        for d in directions:
            nx, ny = cx + d[0], cy + d[1]
            # print(f"nx:{nx}, ny:{ny}")
            # pdb.set_trace()
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if closed_cell[ny][nx] == 1:
                continue
            if (nx, ny) in [c.xy for c in open_cell]:
                nf = curr_cell.f + Map[cy][cx] + Map[ny][nx]
                ng = abs(nx - target[0]) + abs(ny - target[1])
                nh = nf + ng
                if nh < cells[ny][nx].h:
                    cells[ny][nx].parent = (cx,cy)
                    cells[ny][nx].f = nf
                    cells[ny][nx].g = ng
                    cells[ny][nx].h = nh
            else:
                cells[ny][nx].parent = (cx,cy)
                cells[ny][nx].f = curr_cell.f + Map[cy][cx] + Map[ny][nx]
                cells[ny][nx].g = abs(nx - target[0]) + abs(ny - target[1])
                cells[ny][nx].h = cells[ny][nx].f + cells[ny][nx].g
                open_cell.append(cells[ny][nx])
        # pdb.set_trace()
        open_cell = sorted(open_cell, key=lambda x: x.h)
        # print(open_cell)
    
    if result_path:
        # print("->", result_path, ":", result_dist)
        return result_path, result_dist
    else:
        # print("No path found")
        # pdb.set_trace()
        return None

# find l-i-c dist
# = 2 times
l2i_path, l2i_dist = find_path(l_pos, i_pos)
i2c_path, i2c_dist = find_path(i_pos, c_pos)
# print("l-i:",l2i_dist)
# print("i-c:",i2c_dist)
# pdb.set_trace()

# fild e1-l/c-e2, e2-l/c-e1
# = 4 times
# choose min(e1_l+c_e2, e2_l+c_e1)
_, s_e1_dist = find_path((0,0), e1_pos)
_, e1_l_dist = find_path(e1_pos, l_pos)
_, c_e2_dist = find_path(c_pos, e2_pos)
# print("s-e1:",s_e1_dist)
# print("e1-l:",e1_l_dist)
# print("...:", l2i_dist + i2c_dist)
# print("c-e2:",c_e2_dist)

# print("------")
_, s_e2_dist = find_path((0,0), e2_pos)
_, e2_l_dist = find_path(e2_pos, l_pos)
_, c_e1_dist = find_path(c_pos, e1_pos)
# print("s-e2:",s_e2_dist)
# print("e2-l:",e2_l_dist)
# print("...:", l2i_dist + i2c_dist)
# print("c-e1:",c_e1_dist)
# pdb.set_trace()

el_ce_dist = min(s_e1_dist + e1_l_dist + c_e2_dist, s_e2_dist +  e2_l_dist + c_e1_dist)


print(l2i_dist + i2c_dist + el_ce_dist)

