import pdb
import re

# N, M, K = [1,300]
# T = [1, M]
# a,b = [1,N+1]

N, M, K, T = map(int,input().split())
occupied = [0]*N
timetable = [-T]*N
for _ in range(M):
    a, b = map(int,input().split())
    for i in range(a-1,b-1):
        timetable[i] += 1
        occupied[i] += 1

# idx_str = ''
# occ_str = ''
# seat_str = ''
# for i, s in enumerate(timetable):
#     idx_str += str(i+1).rjust(3) + ' '
#     occ_str += str(occupied[i]).rjust(3) + ' '
#     seat_str += str(s).rjust(3) + ' '
# print('  i:', idx_str)
# print('[+]:', occ_str)
# print('[-]:', seat_str)

god = []
for t in timetable:
    if t >= 0: # m god
        god.append('m')
    elif t + K >= 0: # k god
        god.append('k')
    else:
        god.append('-')

god_str = ''.join(god)  
# god_m_str = ''
# god_k_str = ''
# for g in god_str:
#     if g == 'm':
#         god_m_str += g.rjust(3) + ' '
#         god_k_str += '    '
#     elif g == 'k':
#         god_m_str += '    '
#         god_k_str += g.rjust(3) + ' '
#     else:
#         god_m_str += '    '
#         god_k_str += '    '
# print('G_m:', god_m_str)
# print('G_k:', god_k_str)

m_cnt = god_str.count('m')

si = -1
ei = -1
req = 0
k_cnt = 0
k_sections_dict = []
k_sections = []
for i, (g, t) in enumerate(zip(god, timetable)):
    if g == 'k':
        if si == -1:
            si = i
            k_cnt = 1
        else:
            k_cnt += 1
    elif g == 'm':
        if si == -1:
            continue
        else: # si != -1
            ei = i
            reqs = sorted(list(set(timetable[si:ei])))
            ks = []
            for req in reqs:
                score = len([r for r in timetable[si:ei] if r >= req])
                ks.append((req, score))
            k_sections.append(ks)
            
            t_dic = {"time": (si+1,ei), "ks": ks}
            k_sections_dict.append(t_dic)
            
            si = ei = -1
            k_cnt = req = 0
    else: # '-'
        continue
# add last
if si != -1:
    ei = N
    reqs = sorted(list(set(timetable[si:ei])))
    ks = []
    for req in reqs:
        score = len([r for r in timetable[si:ei] if r >= req])
        ks.append((req, score))
    k_sections.append(ks)
    
    t_dic = {"time": (si+1,ei), "ks": ks}
    k_sections_dict.append(t_dic)

# pdb.set_trace()
# print("k_sections")
# print("dict:", k_sections_dict)
# # k_sections.sort(reverse=True)
# print("list:", k_sections)
# pdb.set_trace()

# --> knapsack problem
# large k_cnt when sum(req) not exceed K

def knapsack(k_sections, empty_space):
    # print("k_sections:", k_sections)
    # print("empty_space:", empty_space)
    if not k_sections:
        return 0
    # pdb.set_trace()
    res = []
    for ks in k_sections[0]:
        size, score = ks
        size = -size
        if size > empty_space:
            res.append(knapsack(k_sections[1:], empty_space))
        else:
            res.append(max(knapsack(k_sections[1:], empty_space),
                           score + knapsack(k_sections[1:], empty_space-size)))
    return max(res)
    
k_max = knapsack(k_sections, K)
# print("k_max:", k_max)
# pdb.set_trace()
print(m_cnt + k_max)



