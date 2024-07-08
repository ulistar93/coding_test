# N = [1,999999]
import pdb

def main():
    nstr = input()
    nlist = list(map(int, nstr))
    rlist = nlist[::-1]
    
    # print("nlist: ", nlist)
    # print("rlist: ", rlist)

    # find carrier
    c_idx = -1
    c_val = '0'
    bef = rlist[0]
    for i, c in enumerate(rlist[1:]):
        if bef > c: # descending
            c_idx = i+1
            c_val = c
            break
        else: # assending or equal
            bef = c
            continue
    assert c_idx != -1, "No possible answer"
    
    # replace carrier
    r_idx = -1
    for i, c_ in enumerate(rlist[:c_idx]):
        if c_ > c_val:
            rlist[c_idx], rlist[i] = rlist[i], rlist[c_idx]
            r_idx = i
            # print(f"swap: [{c_idx}]<->[{r_idx}]")
            break 
        else:
            continue
    assert r_idx != -1, "Wrong carrier found"
    
    # print("rlist: ", rlist)
    
    # revese
    small_part = rlist[c_idx-1::-1]
    large_part = rlist[c_idx:]
    # print("small_part: ", small_part)
    # print("large_part: ", large_part)
    new_rlist = small_part + large_part
    new_nlist = new_rlist[::-1]
    # print("new_nlist: ", new_nlist)
    res = int(''.join(map(str, new_nlist)))
    print(res)
    # pdb.set_trace()
    
if __name__ == "__main__":
    main()
