# import numpy as np
# import pdb
# N = [3,20]

N = int(input())
class_room = [[0] * N for _ in range(N)]
class_happiness = [[0] * N for _ in range(N)]
student_seat = {}
student_list = []
like_dict = {}
for _ in range(N*N):
  i, a, b, c, d = map(int,input().split())
  student_list.append(i)
  like_dict[i] = [a, b, c, d]
class_brightness  = [[2] + [3]*(N-2) + [2]]
class_brightness += [[3] + [4]*(N-2) + [3] for _ in range(N-2)]
class_brightness += [[2] + [3]*(N-2) + [2]]
best_bright_pos = (1,1)
best_brightness = 4

def empty_score(seat):
  r,c = seat
  # l = (r,c-1) if c-1>=0 else None
  # n = (r,c+1) if c+1<N else None
  # u = (r-1,c) if r-1>=0 else None
  # d = (r+1,c) if r+1<N else None
  # score = 0
  # score += 1 if l and class_room[l[0]][l[1]] == 0 else 0
  # score += 1 if r and class_room[n[0]][n[1]] == 0 else 0
  # score += 1 if u and class_room[u[0]][u[1]] == 0 else 0
  # score += 1 if d and class_room[d[0]][d[1]] == 0 else 0
  # return score
  return class_brightness[r][c]

def find_like_pos(me, friends):
  roi = {}
  for f in friends:
    if f not in student_seat:
      continue
    r,c = student_seat[f]
    left  = (r,c-1) if c-1>=0 else None
    right = (r,c+1) if c+1<N else None
    up    = (r-1,c) if r-1>=0 else None
    down  = (r+1,c) if r+1<N else None
    
    left  = None if left in student_seat.values() else left
    right = None if right in student_seat.values() else right
    up    = None if up in student_seat.values() else up
    down  = None if down in student_seat.values() else down
    
    if left:
      roi[left] = roi.get(left, 0) + 1
    if right:
      roi[right] = roi.get(right, 0) + 1
    if up:
      roi[up] = roi.get(up, 0) + 1
    if down:
      roi[down] = roi.get(down, 0) + 1
  if len(roi) == 0:
    return None, None
      
  max_prefer = 0
  candi = []
  for c in list(roi.keys()):
    if roi[c] > max_prefer:
      max_prefer = roi[c]
      candi = [c]
    elif roi[c] == max_prefer:
      candi.append(c)
  candi2 = [candi[0]]
  max_empty_score = empty_score(candi[0])
  if len(candi) > 1:
    for c in candi[1:]:
      es = empty_score(c)
      if es > max_empty_score:
        max_empty_score = es
        candi2 = [c]
      elif es == max_empty_score:
        candi2.append(c)
  candi3 = candi2[0]
  if len(candi2) > 1:
    for c in candi2:
      if c[0] < candi3[0]:
        candi3 = c
      elif c[0] == candi3[0]:
        if c[1] < candi3[1]:
          candi3 = c
  return candi3, max_prefer

def add_happiness(me, pos, hp):
  r, c = pos
  class_happiness[r][c] = hp
  left  = (r,c-1) if c-1>=0 else None
  right = (r,c+1) if c+1<N else None
  up    = (r-1,c) if r-1>=0 else None
  down  = (r+1,c) if r+1<N else None
  if left and class_room[left[0]][left[1]] != 0:
    left_id = class_room[left[0]][left[1]]
    if me in like_dict[left_id]:
      class_happiness[left[0]][left[1]] += 1
  
  if right and class_room[right[0]][right[1]] != 0:
    right_id = class_room[right[0]][right[1]]
    if me in like_dict[right_id]:
      class_happiness[right[0]][right[1]] += 1
  if up and class_room[up[0]][up[1]] != 0:
    up_id = class_room[up[0]][up[1]]
    if me in like_dict[up_id]:
      class_happiness[up[0]][up[1]] += 1
  if down and class_room[down[0]][down[1]] != 0:
    down_id = class_room[down[0]][down[1]]
    if me in like_dict[down_id]:
      class_happiness[down[0]][down[1]] += 1

def update_class_brightness(pos):
  r, c = pos
  class_brightness[r][c] = -1
  left  = (r,c-1) if c-1>=0 else None
  right = (r,c+1) if c+1<N else None
  up    = (r-1,c) if r-1>=0 else None
  down  = (r+1,c) if r+1<N else None
  if left:
    class_brightness[left[0]][left[1]] -= 1
  if right:
    class_brightness[right[0]][right[1]] -= 1
  if up:
    class_brightness[up[0]][up[1]] -= 1
  if down:
    class_brightness[down[0]][down[1]] -= 1
  
  global best_bright_pos
  global best_brightness
  best_r, best_c = best_bright_pos
  max_class_brightness = max([max(class_brightness[i]) for i in range(N)])
  if best_brightness != max_class_brightness:
    best_brightness = max_class_brightness
    best_r, best_c = (0,0)
  if best_brightness < 0:
    best_bright_pos = (-1, -1)
    return
  while class_brightness[best_r][best_c] < best_brightness:
    best_c += 1
    if best_c == N:
      best_c = 0
      best_r += 1
    if best_r == N:
      best_r, best_c = (-1, -1)
      break
  best_bright_pos = (best_r, best_c)
  return

def find_best_empty_seat():
  return best_bright_pos

def calculate_happiness():
  # pdb.set_trace()
  total_happiness = 0
  for r in range(N):
    for c in range(N):
      if class_happiness[r][c] == 1:
        total_happiness += 1
      elif class_happiness[r][c] == 2:
        total_happiness += 10
      elif class_happiness[r][c] == 3:
        total_happiness += 100
      elif class_happiness[r][c] == 4:
        total_happiness += 1000
  return total_happiness

def print_class_room():
  print("====class_room====")
  for i in range(N):
    print(class_room[i])

def print_happiness():
  print("====class_happiness====")
  for i in range(N):
    print(class_happiness[i])
    
def print_brightness():
  print("====class_brightness====")
  for i in range(N):
    print(class_brightness[i])
  print("  -> best_bright_pos: ", best_bright_pos)

def main():
  # print_class_room()
  # print_happiness()
  # print_brightness()
  
  for i in student_list:
    # pdb.set_trace()
    fav, happy = find_like_pos(i, like_dict[i])
    if fav:
      class_room[fav[0]][fav[1]] = i
      student_seat[i] = fav
      add_happiness(i, fav, happy)
      update_class_brightness(fav)
    else:
      seat = find_best_empty_seat()
      if seat == (-1, -1):
        assert False, "No more seat"
      class_room[seat[0]][seat[1]] = i
      student_seat[i] = seat
      add_happiness(i, seat, 0)
      update_class_brightness(seat)
    # print_class_room()
    # print_happiness()
    # print_brightness()
  print(calculate_happiness())

main()