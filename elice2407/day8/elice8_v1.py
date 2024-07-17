import pdb

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

idx_str = ''
occ_str = ''
seat_str = ''
for i, s in enumerate(timetable):
    idx_str += str(i+1).rjust(3) + ' '
    occ_str += str(occupied[i]).rjust(3) + ' '
    seat_str += str(s).rjust(3) + ' '
print('  i:', idx_str)
print('[+]:', occ_str)
print('[-]:', seat_str)
pdb.set_trace()


maximum_len = 0
m_god = 0 # m > T
k_god = 0 # m + k > T
god_len_mk = 0 # m -> k
god_len_km = 0 # k -> m
m_list = []
k_list = []
god_mk_list = []
god_km_list = []
for i, t in enumerate(timetable):
    if t >= 0: # m god
        m_god += 1
        if k_god:
            god_len_mk += k_god
            god_len_km = k_god
        k_god = 0
    elif t + K >= 0: # k god
        k_god += 1
        if m_god:
            god_len_km += m_god
            god_len_mk = m_god
        m_god = 0
    m_list.append(m_god)
    k_list.append(k_god)
    god_mk_list.append(god_len_mk)
    god_km_list.append(god_len_km)
    
    if god_len_mk > maximum_len:
        maximum_len = god_len_mk
    if god_len_km > maximum_len:
        maximum_len = god_len_km

if k_god:
    god_len_mk += k_god
    # god_mk_list[-1] = god_len_mk
    if god_len_mk > maximum_len:
        maximum_len = god_len_mk
if m_god:
    god_len_km += m_god
    # god_km_list[-1] = god_len_km
    if god_len_km > maximum_len:
        maximum_len = god_len_km

print("     m_list:", m_list)
print("     k_list:", k_list)
print("god_mk_list:", god_mk_list)
print("god_km_list:", god_km_list)
pdb.set_trace()

print(maximum_len)
pdb.set_trace()
