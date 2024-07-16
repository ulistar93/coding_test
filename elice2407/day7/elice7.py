import pdb


def main():
    N, K = map(int, input().split())
    Na = N + 1

    # 101 4 -> 1234
    if Na < 10**(K-1):
        Na = 10**(K-1)

    res = replaceX(Na,K)
    # 998 2 -> 1000
    # 998 3 -> 1002
    # 987 3 -> 990 -> 1000 -> 1002
    # 978 3 -> 980
    # 498 3 -> 500 -> 501
    while res < 0:
        cloc = -res
        carry = 10 ** cloc
        rest = Na % carry
        Na -= rest
        Na += carry
        # print(f" **res<0** -> cloc={cloc}, carry={carry}, rest={rest}, New Na={Na}")
        res = replaceX(Na, K)
    # if res > 10**7:
    #     res = N
    print(res)


def replaceX(Na,K) -> int:
    Nas = str(Na)
    ck = len(set(Nas))

    rep_ridx = 0
    rep_ox = [] # 1: add ck, 0: no count 
    while ck != K:
        rep_ridx +=1
        if rep_ridx > len(Nas):
            # pdb.set_trace()
            return "ERROR" # not gonna happen <- prevented by 10**(K-1)
        sub_Nas = Nas[:-rep_ridx]
        if ck > K: # reduce ck
            rep_ox.append(0)
        else: # ck < K # increase ck
            rep_ox.append(1)
        ck = len(set(sub_Nas)) + sum(rep_ox)
    rep_ox = rep_ox[::-1]

    if not rep_ridx:
        return Na
    
    front_Nas = Nas[:-rep_ridx]
    used = set(map(int,front_Nas))
    all_set = set(range(10))
    unused = all_set - used
    # print("    Na:", Nas)
    # print(f"rep({rep_ridx})".rjust(8) + ' '*(len(Nas)-rep_ridx), end='')
    # for ox in rep_ox[::-1]:
    #     print('o' if ox else 'x', end='')
    # print()
    # print("  used:", used)
    # print("unused:", unused)
    # pdb.set_trace()
    
    new_Nstr = '' + front_Nas
    upper = False
    for i, ri in enumerate(range(rep_ridx,0,-1)):
        orgN = Nas[-ri]
        lset = set([ x for x in range(10) if x >= int(orgN)]) if not upper else set(range(10))
        # print(" *lset:", lset)
        # print(" *useX:", unused)
        # print(" *used:", used)
        candi = lset
        if rep_ox[i]: # o
            candi &= unused
        else: # x
            candi &= used
        if not candi:
            # pdb.set_trace()
            return -ri # can not be smaller
        # print(" *candi:", candi)
        newN = min(candi)
        # print("   N:", Nas)
        # ox = 'o' if rep_ox[i] else 'x'
        # print(" rep:", ' '*(len(Nas)-rep_ridx) + ox, end='')
        # print(" ->", newN)
        used.add(newN)
        unused = all_set - used
        new_Nstr += str(newN)
        if upper == False and newN > int(orgN):
            upper = True
        # pdb.set_trace()
        
    return int(new_Nstr)

main()
