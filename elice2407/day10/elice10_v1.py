# import pdb

def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)

# N = int(input())
A = list(map(int,input().split()))
N = len(A)

ArgA = argsort(A)

print_tf = True

checklist = [0]*N
k_str = ''
k = 0
max_k = 0
while True:
    # print(ArgA)
    if ArgA == []:
        break
    top_idx = ArgA.pop()
    top_value = A[top_idx]
    if checklist[top_idx] == 1:
        # some part of other mountain -> skip
        continue
    if top_value <= max_k:
        # smaller mountain than before -> finish
        break
    
    top_pyramid = [0] * top_value
    top_pyramid[-1] = 1
    checklist[top_idx] = 1
    right_idx = top_idx + 1
    while right_idx < N:
        right_value = A[right_idx]
        right_insert = False
        if right_value > top_value:
            while len(top_pyramid) < right_value:
                top_pyramid.append(0)
        for l in range(right_value, -1, -1):
            if top_pyramid[l-1] != 1:
                top_pyramid[l-1] = 1
                right_insert = True
                break
        if right_insert:
            checklist[right_idx] = 1
        else: # no empty space below right_value
            break # break right while
        right_idx += 1
    left_idx = top_idx - 1
    while left_idx >= 0:
        left_value = A[left_idx]
        left_insert = False
        if left_value > top_value:
            while len(top_pyramid) < left_value:
                top_pyramid.append(0)
        for l in range(left_value, -1, -1):
            if top_pyramid[l-1] != 1:
                top_pyramid[l-1] = 1
                left_insert = True
                break
        if left_insert:
            checklist[left_idx] = 1
        else: # no empty space below left_value
            break # break left while
        left_idx -= 1
        
        
    # k = top_pyramid.index(0) + 1 if 0 in top_pyramid else len(top_pyramid)
    k = sum(top_pyramid)
    
    # print
    if print_tf:
        left_valid_idx = left_idx + 1
        right_valid_idx = right_idx - 1
        print(''.join([str(x).rjust(3) for x in A]))
        vx_str = ['   '] * N
        vx_str[left_valid_idx] = '  o'
        for i in range(left_valid_idx+1, right_valid_idx):
            vx_str[i] = '---'
        vx_str[top_idx] = '--^'
        if left_valid_idx == top_idx:
            vx_str[left_valid_idx] = ' o^'
        vx_str[right_valid_idx] = '--o'
        if right_valid_idx == top_idx:
            vx_str[right_valid_idx] = '--^o'
        print(''.join(vx_str))
        print("xl-top-rx:", left_idx, top_idx, right_idx)
        print("pyramid:",top_pyramid)
        print("k:", k)
    max_k = max(max_k, k)
          
    # pdb.set_trace()
    
# print("end of all")
print(max_k)
# pdb.set_trace()
