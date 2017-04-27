
cc2 = [[0, 2, 9, float("inf")], [1, 0, 6, 4], [float("inf"), 7, 0, 8], [6, 3, float("inf"), 0]]
cc3 = [[0, 14, 4, 10, 20],[14, 0, 7, 8, 7],[4, 5, 0, 7, 16],[11, 7, 9, 0, 2],[18, 7, 17, 4, 0]]
#start_path = []
'''
def pathfinder(weight, start, cities, matrix):
    path = start_path
    tbvisited = []
    for i in cities: 
        if i not in start_path:
            tbvisited.append(i)

    #tbvisited.append(start)
    weight = weight - matrix[start_path[0]][start_path[1]] - matrix[start_path[1]][start_path[2]]
     
    #for i in matrix[start_path[-1]]:
        
    
    print("cur_weight: " + str(weight))
    print("tbvisit: " + str(tbvisited))
    print("start_path: " + str(start_path))
'''
def rmel(ls, index):
    return ls[:index] + ls[index+1:]

def subtsp(target, comp, matrix):
    if len(comp) == 1:
        #if len(start_path) < 3:
        #    start_path.append(target)
        return matrix[comp[0]][target] + matrix[0][comp[0]]
    elif len(comp) != 0:
        temp = float("inf")
        for i in range(0, len(comp)-1):
            temp = min(temp,
                    matrix[comp[i]][target] + subtsp(comp[i], rmel(comp, i), matrix),
                    matrix[comp[i+1]][target] + subtsp(comp[i+1], rmel(comp, i+1), matrix))
            #if target not in start_path: #DOES NOT WORK FOR CC3
             #   start_path.append(target)
    return temp 

def tsp(matrix):
    cities = []
    start_node = 0 #LET USER INPUT START NODE AND ADD ERROR CHECKING FOR CC1 AND CC2 
    
    # Adds all nodes except for the start node to cities
    for i in range(0, len(matrix)):
        if i != start_node:
            cities.append(i)

    #start_path.append(start_node)
    my_tsp = subtsp(start_node, cities, matrix)
    print("Weight: " + str(my_tsp))
    #print("Path: " + str(pathfinder(my_tsp, start_node, cities, matrix)))
    #start_path.append(start_node)
    #print([x+1 for x in start_path])



tsp(cc3)
