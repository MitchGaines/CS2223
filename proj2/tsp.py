
cc2 = [[0, 2, 9, float("inf")], [1, 0, 6, 4], [float("inf"), 7, 0, 8], [6, 3, float("inf"), 0]]
cc3 = [[0, 14, 4, 10, 20],[14, 0, 7, 8, 7],[4, 5, 0, 7, 16],[11, 7, 9, 0, 2],[18, 7, 17, 4, 0]]
#matrix = [[0, 2, 9, -100], [1, 0, 6, 4], [-100, 7, 0, 8], [6, 3, -100, 0]]

def rmel(ls, index):
    return ls[:index] + ls[index+1:]

def subtsp(target, comp, matrix):
    if len(comp) == 1:
        return matrix[comp[0]][target] + matrix[0][comp[0]]
    elif len(comp) != 0:
        temp = float("inf")
        for i in range(0, len(comp)-1):
            temp = min(temp, matrix[comp[i]][target] + subtsp(comp[i], rmel(comp, i), matrix), matrix[comp[i+1]][target] + subtsp(comp[i+1], rmel(comp, i+1), matrix))
            
    return temp 

def tsp(matrix):
    c_vals = []
    for i in range(1, len(matrix)):
        c_vals.append(i)
    
    print(subtsp(0, c_vals, matrix))

tsp(cc2)
