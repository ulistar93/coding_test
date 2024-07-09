# n m
#   n = [1,10000], m = [1,500]
# i j k
#   i,j = [1,n]
#   k = [1,j-i+1]

# import pdb

def argsort(_list:list):
    return sorted(range(len(_list)), key=lambda i: _list[i])
    # return sorted(range(len(_list)), key=_list.__getitem__)

def ver1(all_list, n, i, j, k):
    '''
      nlogn + n + m + mlogm 
    '''
    argsort_list = argsort(all_list)
    rank_list = [0] * n
    for idx, val in enumerate(argsort_list):
        rank_list[val] = idx
    # print("** all_list     :", all_list)
    # print("** argsort_list :", argsort_list)
    # print("** rank_list    :", rank_list)

    all_list_sub = all_list[i-1:j]
    # print("all_list_sub   :", all_list_sub)
    rank_list_sub = rank_list[i-1:j]
    min_idx = min(rank_list_sub)
    rank_list_sub = [x - min_idx for x in rank_list_sub]
    # print("rank_list_sub  :", rank_list_sub)
    rank_list_args = argsort(rank_list_sub)
    # print("rank_list_args :", rank_list_args)
    k_idx = rank_list_args[k-1]
    # k_idx = rank_list_sub.index(k-1)
    res = all_list_sub[k_idx]
    # print("k_idx :", k_idx, ", res :", res)
    return res

def ver2(all_list, n, i, j, k):
    '''
      mlogm 
    '''
    # print("** all_list :", all_list)

    all_list_sub = all_list[i-1:j]
    # print("all_list_sub     :", all_list_sub)
    argsort_list_sub = argsort(all_list_sub)
    # print("argsort_list_sub :", argsort_list_sub)
    k_idx = argsort_list_sub[k-1]
    res = all_list_sub[k_idx]
    # print("k_idx :", k_idx, ", res :", res)
    return res

def main():
    n, m = map(int,input().split())
    all_list = list(map(int, input().split()))
    results = []
    for _ in range(m):
        i, j, k = map(int, input().split())
        # i, j start with 1~n
        # res = ver1(all_list, n, i, j, k)
        res = ver2(all_list, n, i, j, k)
        results.append(res)
    for i in range(len(results)):
        print(results[i])

if __name__ == "__main__":
    main()
