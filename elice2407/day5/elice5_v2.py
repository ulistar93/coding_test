import pdb
import time

def main():
    N = int(input())
    # subset sum
    sss = list(map(int,input().split()))

    start = time.time()
    ssss = sorted(sss) # sorted sss
    
    arr = []
    ss = ssss
    while len(arr) < N:
        check_list = [0] * len(ss)
        a = ss[1]
        arr.append(a)
        # print('*arr:',arr)
        # print('       ss :',ss)
        # print('check_list:',check_list)
        # print('        i(0) ' + '^')
        xlist = [ss[0]]
        olist = [ss[1]]
        check_list[0] = check_list[1] = 1
        # print('check_list:',check_list)
        # print('        i(0) ' + 'x  x')
        # print(' -> xlist :',xlist)
        # print(' -> olist :',olist)
        # print('          ----')
        # pdb.set_trace()
        idx = 2
        ss_t = ss[idx:]
        while len(ss_t) > 0:
            if check_list[idx]:
                idx += 1
                ss_t = ss_t[1:]
                continue
            # print('       ss :',ss)
            # print('check_list:',check_list)
            # print(f'idx({idx}) '.rjust(13) + ' '*(3*idx) + '^')
            # print('     ss_t :' + ' '*(3*idx), ss_t)
            # pdb.set_trace()
            # add s into xlist
            s = ss_t[0]
            xlist.append(s)
            check_list[idx] = 1
            # find s+a
            try:
                o_loc = 1 + ss_t[1:].index(s+a)
                while check_list[idx+o_loc]:
                    o_loc += 1 + ss_t[o_loc+1:].index(s+a)
            except ValueError:
                pdb.set_trace()
            olist.append(ss_t[o_loc])
            check_list[idx + o_loc] = 1
            # print('     ss_t :' + ' '*(3*idx), ss_t)
            # print('check_list:',check_list)
            # print(f'idx({idx}) '.rjust(13) + ' '*(3*idx) + 'x  ' + ' '*(3*(o_loc-1)) + 'x')
            # print(' -> xlist :',xlist)
            # print(' -> olist :',olist)
            # print('          ----')
            # pdb.set_trace()
            idx += 1
            ss_t = ss_t[1:]
        # print('=================================')
        # print(' * arr(a) :',arr)
        # print(' -> xlist :',xlist)
        # pdb.set_trace()
        ss = xlist
    # print("**fin arr:",arr)
    print(" ".join(list(map(str, arr))))
    # pdb.set_trace()
    end = time.time()
    print(f"Time: {end-start}")

if __name__=="__main__":
    main()
