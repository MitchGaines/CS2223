
#each row represents an edge as follows: [weight, start, end]
edges = [[17, 1, 4], [32, 1, 2], [45, 2, 5], [10, 4, 5], [18, 3, 4], [5, 3, 7], [59, 7, 8], [3, 4, 8], [4, 8, 9], [25, 5, 9], [28, 5, 6], [6, 6, 10], [12, 9, 10]]

def val_exist(element, ls):
    if element in ls:
        return 1 
    else:
        return 0

def rm_rows(ls, vals):
    temp = []
    for i in range(0, len(ls)):
        if not(val_exist(ls[i][1], vals) or val_exist(ls[i][2], vals)):
            temp.append(ls[i])

    return temp

def rm_row(ls, index):
    ls.pop(index)
    return ls

def get_edges_index(edges, ls):
    for i in range(0, len(edges)):
        if set(edges[i]) == set(ls):
            return i

def get_unique_nodes(edges):
    vals = []
    for i in edges:
        vals.append(i[1])
        vals.append(i[2])

    vals = set(vals)
    return vals

def prim(edges):
    mst = []
    active_list = []
    curr_nodes = [1]
    all_nodes = get_unique_nodes(edges)
    mod_edges = edges
    active_list_new = active_list

    while (len(curr_nodes) < len(all_nodes)-1):
       # print("Edges: " + str(edges))
       # print("Active List: " + str(active_list)) 
        #search edges for selected nodes and add to active list
        for i in range(0, len(edges)):
            for j in range(0, len(curr_nodes)):
                if edges[i][1] == curr_nodes[j] or edges[i][2] == curr_nodes[j]:
                    active_list.append(edges[i])
                    #print(active_list)
                    #print("\n\n-------- \n\n")

        mod_edges = rm_rows(mod_edges, curr_nodes)

        curr_min = float("inf")
        curr_min_index = -1
        #search active list for smallest weighted edge
        for i in range(0, len(active_list)):
            if curr_min > active_list[i][0]:
                curr_min = active_list[i][0]

        #look for curr_min's row and add that to mst and its brother node to curr_nodes
        for i in range(0, len(active_list)):
            if curr_min == active_list[i][0]:
                curr_min_index = i
                mst.append(active_list[i])
                if active_list[i][1] in curr_nodes:
                    curr_nodes.append(active_list[i][2]) # NOT WORKING HERE, NOT ADDING PARTNER NODES
                elif active_list[i][2] in curr_nodes:
                    curr_nodes.append(active_list[i][1])
                #edges = rm_row(edges, get_edges_index(edges, active_list[i]))
        
        active_list_new = rm_row(active_list, curr_min_index) 
        edges = mod_edges
        active_list = active_list_new
    
    print("MST: " + str(mst))

prim(edges)

