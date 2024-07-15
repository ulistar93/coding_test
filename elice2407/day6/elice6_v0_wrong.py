# v0 : wrong
# 6, 000000 -> 15 X

N = int(input())
line_colors = list(map(int,input().split()))

red_score = 0
groups = [1] * N
print('-', groups)

def move_blue():
    global groups
    t = groups[0] + groups[1]
    groups = groups[1:]
    groups[0] = t
    print('1', groups)
    return

def move_red():
    global red_score
    global groups
    s = groups[-1] * groups[-2]
    t = groups[-1] + groups[-2]
    groups = groups[:-2]
    groups.append(t)
    groups.sort(reverse=True)
    red_score += s
    print('0', groups, " -> red_score +=", s)
    return

for line in line_colors:
    if line:
        move_blue()
    else:
        move_red()

print(red_score)
