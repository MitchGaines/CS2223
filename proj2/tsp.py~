
matrix = [[0, 2, 9, float("inf")], [1, 0, 6, 4], [float("inf"), 7, 0, 8], [6, 3, float("inf"), 0]]

#matrix = [[0, 2, 9, -100], [1, 0, 6, 4], [-100, 7, 0, 8], [6, 3, -100, 0]]

def rmel(ls, index):
    return ls[:index] + ls[index+1:]

def subtsp(target, comp):
    if len(comp) == 1:
        return matrix[comp[0]][target] + matrix[0][comp[0]]
    elif len(comp) != 0:
        for i in range(0, len(comp)-1):
            temp = matrix[comp[i]][target] + subtsp(comp[i], rmel(comp, i))
            temp = min(temp, matrix[comp[i+1]][target] + subtsp(comp[i+1], rmel(comp, i+1)))
            
    return temp 

def tsp():
    print(subtsp(0, [1, 2, 3]))

tsp()
