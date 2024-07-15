# v1 : right but complicate
import itertools
import time

from collections import Counter

print1 = print
import pdb
# print = lambda *args : None # print override
# class pdb: # pdb override
#     def set_trace():
#         pass

N = int(input())
line_colors = list(map(int,input().split()))

nodes = []
nodes.append([[1]*N])
node_slist = []
node_slist.append(['1'*N])
edges = {}
print("---------------- find node & edge")
start = time.time()
for step in range(N-1):
    parent_list = nodes[-1]
    child_list = []
    child_str_list = []
    for parent in parent_list:
        # print("nodes    :", nodes)
        # print("parent   :", parent)
        parent_str = ''.join(map(str,parent))
        shrinked_parent = list(set(parent))
        counter = Counter(parent)
        dup = [o for o, c in counter.items() if c > 1]
        shrinked_parent += dup
        combinations = set(itertools.combinations(shrinked_parent, 2))
        # combinations = set(itertools.combinations(parent,2))
        for (u, v) in combinations:
            child = parent.copy()
            child.remove(u)
            child.remove(v)
            child.append(u+v)
            child.sort(reverse=True)
            child_str = ''.join(map(str,child))
            if child not in child_list:
                child_list.append(child)
                child_str_list.append(child_str)
            # else:
            #     print(" *child exist")
            #     pdb.set_trace()
            edge_str = parent_str + '->' + child_str
            if edge_str not in edges:
                edges[edge_str] = u*v
            # else:
            #     print(" *edge exist")
            #     pdb.set_trace()
            # print(f"  {u}+{v}:", child)
            # print(f"  {edge_str}:",u*v)
        pass
    nodes.append(child_list)
    node_slist.append(child_str_list)
    # print(" -> nodes:", nodes)
    # print(" -> edges:", edges)
    # pdb.set_trace()
    pass
end = time.time()
# print(" -> nodes:", nodes)
# print("-> node_slist:", node_slist)
# print("-> edges:", edges)

elapsed = end - start
print(f"---- {elapsed}")

print(f"---------------- rename index")
start = time.time()
node_name2index = {}
node_index2name = []
idx = 0
for node_list in node_slist:
    for node in node_list:
        if node not in node_name2index:
            node_name2index[node] = idx
            node_index2name.append(node)
            idx += 1

edges_int2int = {}
edges_tuplecost = {}
for edge in edges:
    u, v = edge.split('->')
    uidx = node_name2index[u]
    vidx = node_name2index[v]
    if uidx in edges_int2int:
        edges_int2int[uidx].append(vidx)
    else:
        edges_int2int[uidx] = [vidx]
    edges_tuplecost[(uidx, vidx)] = edges[edge]

end = time.time()
# print("-> node_name2index:", node_name2index)
# print("-> node_index2name:", node_index2name)
# print("-> edges_int2int:", edges_int2int)
# print("-> edges_tuplecost:", edges_tuplecost)

elapsed = end - start
print(f"---- {elapsed}")

print("---------------- dfs")
start = time.time()
def dfs_costy(myIdx, costy, line_rb):
    if costy[myIdx] != -1: # visited
        return costy[myIdx]
    else: # not visited
        if myIdx in edges_int2int and len(line_rb) > 0:
            line_color = line_rb[0]
            child_costs = []
            for child in edges_int2int[myIdx]:
                me2child_cost = edges_tuplecost[(myIdx, child)]
                if line_color:
                    child_costs.append(dfs_costy(child, costy, line_rb[1:]))
                else:
                    child_costs.append(me2child_cost+dfs_costy(child, costy, line_rb[1:]))
            child_cost_min = min(child_costs)
            # print("myIdx:", myIdx, f"<-{line_color}-", child_costs)
            # print("return", child_cost_min)
            costy[myIdx] = child_cost_min
            # print(" -> costy:", costy)
            # pdb.set_trace()
            return costy[myIdx]
        else: # leaf
            # print("myIdx:", myIdx, "-> leaf")
            # print("return 0")
            costy[myIdx] = 0
            # print(" -> costy:", costy)
            # pdb.set_trace()
            return 0

min_cost = dfs_costy(0,[-1] * len(node_index2name),  line_colors)
end = time.time()
elapsed = end - start
print(f"---- {elapsed}")

print1(min_cost)
