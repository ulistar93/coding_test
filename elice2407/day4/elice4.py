# import pdb

tree_rank = []
tree = []
rev_tree = []
tree_score = []
tree_win = []

def argsort(array:list):
    return sorted(range(len(array)), key=lambda x:array[x])

def fill_tree_rank_foward(child:list, parent_lv:int):
    global tree_rank
    if len(child) == 2:
        c0 = child[0]
        c1 = child[1]
        tree_rank[c0] = tree_rank[c1] = parent_lv - 1
        fill_tree_rank_foward(tree[c0], parent_lv - 1)
        fill_tree_rank_foward(tree[c1], parent_lv - 1)
    elif len(child) == 1:
        c0 = child[0]
        tree_rank[c0] = parent_lv - 1
        fill_tree_rank_foward(tree[c0], parent_lv - 1)
    else: # len == 0
        pass
    return

def fill_tree_rank_backward(parent:list, child_lv:int):
    global tree_rank
    if len(parent) == 2:
        c0 = parent[0]
        c1 = parent[1]
        tree_rank[c0] = tree_rank[c1] = child_lv + 1
        fill_tree_rank_foward(rev_tree[c0], child_lv + 1)
        fill_tree_rank_foward(rev_tree[c1], child_lv + 1)
    elif len(parent) == 1:
        c0 = parent[0]
        tree_rank[c0] = child_lv - 1
        fill_tree_rank_foward(rev_tree[c0], child_lv + 1)
    else: # len == 0
        pass
    return

def main():
    N = int(input())
    global tree
    global rev_tree
    global tree_rank
    tree = [[] for _ in range(N)]
    rev_tree = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int,input().split())
        u, v = u-1, v-1
        tree[u].append(v)
        rev_tree[v].append(u)
    tree_rank = [0] * (N)
    # print("tree:", tree)
    # print("rev_tree:", rev_tree)
    
    fill_tree_rank_foward(tree[0], 0)
    fill_tree_rank_backward(rev_tree[0], 0)
    # print("tree_rank:", tree_rank)
    tree_order = argsort(tree_rank)
    # print("tree_order:", tree_order)


    global tree_score
    global tree_win
    tree_score = [[] for _ in range(N)]
    tree_win = [-1] * N
    # tree_score = [[-1] for _ in range(N)]
    # pdb.set_trace()
    for me in tree_order:
        # print("me:",me)
        # print(" -> child:",tree[me])
        # get child score list
        child_score_list = []
        for c in tree[me]:
            child_score_list += tree_score[c]
        # print("child_score_list:", child_score_list)
        # pdb.set_trace()
        child_score_list_new = []
        for c in child_score_list:
            child_score_list_new.append(-c+me)
        if len(child_score_list_new) == 0:
            child_score_list_new = [me]
        # print("child_score_list_new:", child_score_list_new)
        tree_score[me] = child_score_list_new
        if max(child_score_list_new) >= 0:
            tree_win[me] = 1
            # print(" => win")
        else:
            tree_win[me] = 0
            # print(" => Lose")
        # pdb.set_trace()

    # print("tree_win:", tree_win)
    # pdb.set_trace()
    for i in tree_win:
        print(i)

if __name__ == "__main__":
    main()