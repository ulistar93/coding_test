
L='('
R=')'

def find_string_length(s):
    if L in s:
        li = s.index(L)
        rev_ri = s[::-1].index(R)
        ri = len(s) - rev_ri - 1
        sub = s[li+1:ri]
        len_sub = find_string_length(sub)
        multiplier = int(s[li-1])
        return (li-1) + multiplier * len_sub + rev_ri
    else:
        return len(s)

def main():
    org = input()
    print(find_string_length(org))
    return

if __name__ == "__main__":
    main()
