
#each row represents an edge as follows: [weight, start, end]
edges = [[17, 1, 4], [32, 1, 2], [45, 2, 5], [10, 4, 5], [18, 3, 4], [5, 3, 7], [59, 7, 8], [3, 4, 8], [4, 8, 9], [25, 5, 9], [28, 5, 6], [6, 6, 10], [12, 9, 10]]

def val_exist(element, ls):
    if element in ls:
        return 1 
    else:
        return 0

#returns a 2d list without rows 
def rm_rows_with_vals(ls, vals):
    temp = []
    for i in range(0, len(ls)):
        if not(val_exist(ls[i][1], vals) or val_exist(ls[i][2], vals)):
            temp.append(ls[i])

    return temp

#returns a 2d list without rows of given index values
def rm_rows_with_indexes(ls, indexes):
    temp = []
    for i in range(0, len(ls)):
        if i not in indexes:
            temp.append(ls[i])

    return temp

#gets the index of an edge from the edge list
def get_edges_index(edges, ls):
    for i in range(0, len(edges)):
        if set(edges[i]) == set(ls):
            return i

#creates a list of all the nodes in the list of edges
def get_unique_nodes(edges):
    vals = []
    for i in edges:
        vals.append(i[1])
        vals.append(i[2])

    vals = set(vals)
    return vals

#implements prim's algorithm
def prim(edges):
    mst = []
    active_list = []
    curr_nodes = [1]
    all_nodes = get_unique_nodes(edges)
    mod_edges = edges
    active_list_new = active_list

    while (len(curr_nodes) <= len(all_nodes)+2):
        #search edges for selected nodes and add to active list
        for i in range(0, len(edges)):
            for j in range(0, len(curr_nodes)):
                if (edges[i][1] == curr_nodes[j] and edges[i][2] not in curr_nodes) or (edges[i][2] == curr_nodes[j] and edges[i][1] not in curr_nodes):
                    active_list.append(edges[i])

        mod_edges = rm_rows_with_vals(mod_edges, curr_nodes)

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
                #only add if and only if one element is in curr_nodes and one element is not
                if (active_list[i][1] not in curr_nodes) ^ (active_list[i][2] not in curr_nodes):
                    mst.append(active_list[i])
                added_node = -1
                if active_list[i][1] in curr_nodes:
                    added_node = active_list[i][2]
                    curr_nodes.append(added_node)  
                elif active_list[i][2] in curr_nodes:
                    added_node = active_list[i][1]
                    curr_nodes.append(added_node)

        active_list_new = rm_rows_with_indexes(active_list, [curr_min_index])
        edges = mod_edges
        active_list = active_list_new
    
    print("MST: " + str(mst))

prim(edges)
