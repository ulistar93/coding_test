import pdb
import re

# N, M, K = [1,300]
# T = [1, M]
# a,b = [1,N+1]

N, M, K, T = map(int,input().split())
# occupied = [0]*N
timetable = [-T]*N
for _ in range(M):
    a, b = map(int,input().split())
    for i in range(a-1,b-1):
        timetable[i] += 1
        # occupied[i] += 1

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
# pdb.set_trace()

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
# pdb.set_trace()
k_rex = re.findall(r'[k]+[\-]*[k]*', god_str)
# pdb.set_trace()
k_res = list(set(k_rex))
k_max = 0
for kk in k_rex:
    k_cnt = kk.count('k')
    if k_cnt > k_max:
        k_max = k_cnt
        
print(m_cnt + k_max)
