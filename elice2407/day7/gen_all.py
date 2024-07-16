from itertools import product
from tqdm import tqdm
import pdb

# N = 10000000 # 10**7
N = 100000 # 10**5
# N = 100 # 10**5
K = 10
answer_list = [[0] * K for _ in range(N)] # N's answers -> [k=1, ..., 10]
# minimum_list = [-1] * 10
minimum_list = [
    99999,
    99998,
    99987,
    99876,
    98765,
    -1,
    -1,
    -1,
    -1,
    -1
    ]

pdb.set_trace()
for n in range(N,0,-1):
    ck = len(set(str(n)))
    print(n, ck)
    # pdb.set_trace()
    # update min
    answer_list[n-1] = minimum_list.copy()
    minimum_list[ck-1] = n
    print(minimum_list)

pdb.set_trace()

with open('all_cases.txt', 'w') as f:
    for n in tqdm(range(N)):
        for k in range(K):
            if answer_list[n][k] == -1 or answer_list[n][k] <= n+1:
                continue
            f.write(f"{n+1} {k+1} -> {answer_list[n][k]}\n")