
cc2 = [[0, 2, 9, float("inf")], [1, 0, 6, 4], [float("inf"), 7, 0, 8], [6, 3, float("inf"), 0]]
cc3 = [[0, 14, 4, 10, 20],[14, 0, 7, 8, 7],[4, 5, 0, 7, 16],[11, 7, 9, 0, 2],[18, 7, 17, 4, 0]]
start_path = []

def pathfinder(weight, start, cities, matrix):
    path = start_path
    tbvisited = []
    for i in cities: 
        if i not in start_path:
            tbvisited.append(i)

    #tbvisited.append(start)
    weight = weight - matrix[start_path[0]][start_path[1]] - matrix[start_path[1]][start_path[2]]
     
    #for i in matrix[start_path[-1]]:
        
    
    #print("cur_weight: " + str(weight))
    #print("tbvisit: " + str(tbvisited))
    #print("start_path: " + str(start_path))


#removes an element of a list with given index
def rmel(ls, index):
    return ls[:index] + ls[index+1:]

#solves subproblems of tsp
def subtsp(target, comp, matrix):
    if len(comp) == 1:
        #get the first 2 nodes touched by the salesman
        if len(start_path) < 3:
            start_path.append(target)
        
        return matrix[comp[0]][target] + matrix[0][comp[0]]
    elif len(comp) != 0:
        temp = float("inf")

        #throw all the subproblems and their corresponding cities into a 2d list
        subs = []
        for i in range(0, len(comp)):
            subproblem = matrix[comp[i]][target] + subtsp(comp[i], rmel(comp, i), matrix)
            subs.append([subproblem, comp[i]])


        temp_city = -1
        temp_small = float("inf")
        for i in range(0, len(subs)):
            if subs[i][0] < temp_small:
                temp_small = subs[i][0]
                temp_city = subs[i][1]
       
        if temp_city > 0 and temp_city not in start_path:
            start_path.append(temp_city)
        temp = temp_small
    return temp 

def tsp(matrix):
    cities = []
    start_node = 0 #LET USER INPUT START NODE AND ADD ERROR CHECKING FOR CC1 AND CC2 
    
    # Adds all nodes except for the start node to cities
    for i in range(0, len(matrix)):
        if i != start_node:
            cities.append(i)

    start_path.append(start_node)
    my_tsp = subtsp(start_node, cities, matrix)
    print("Weight: " + str(my_tsp))
    start_path.append(start_node)
    print("Path: " + str([x+1 for x in start_path]))



tsp(cc2)
