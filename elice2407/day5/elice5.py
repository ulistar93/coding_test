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
        for i, s in enumerate(ss):
            if check_list[i]: # 1
                continue
            # print('       ss :',ss)
            # print('check_list:',check_list)
            # print(f'i({i}) '.rjust(13) + ' '*(3*i) + '^')
            # pdb.set_trace()
            # add s into xlist
            xlist.append(s)
            check_list[i] = 1
            # find s+a
            o_loc = i + ss[i:].index(s+a)
            while check_list[o_loc]:
                o_loc += 1 + ss[o_loc+1:].index(s+a)
            olist.append(ss[o_loc])
            check_list[o_loc] = 1
            # print('       ss :',ss)
            # print('check_list:',check_list)
            # print(f'i({i}) '.rjust(13) + ' '*(3*i) + 'x  ' + ' '*(3*(o_loc-i-1)) + 'x')
            # print(' -> xlist :',xlist)
            # print(' -> olist :',olist)
            # print('          ----')
            # pdb.set_trace()
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
