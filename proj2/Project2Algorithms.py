## Kylie Dickinson, Alp Piskin, Davaid Abraham, Robi, Mitch
## Algorithms - CS2333
## Project 2 - Gompei's Widget Company
## This project looks at three different algorithms to solve various graphs. It
## has a menu that allows for a user to see the various graphs being tested for
## time efficiencies and sees their outputs for shortest routes, etc. See the
## readme.txt file to understand how to use the menu.


# imports
import time

print("Welcome to Gompei's Widget Company Project, type 'menu()' to coninue")


##*************************************MENU************************************
def menu():
    print("\n----------------------------------MENU-----------------------------------")

    # Ask user questions for use
    print("Please chose one of the following by entering the corresponding number")
    print("1 Prim's Algorithm (Solve Minumum Spanning Tree)")
    print("2 Kruskal's Algorithm (Solve Minimum SPanning Tree)")
    print("3 Prim's Shortest Path (input own start and end nodes)")
    print("4 Kruskal's Shortest Path (input own start and end nodes)")
    print("5 Prim and Kruskal Time Efficiency Comparing MST's")
    print("6 Traveling Salesman Menu")
    print("7 QUIT")
    print("---------------------------------------------------------------------------")
    # Variable Input
    C = int(input("Your choice: "))

    # Choice picked will...
    # If '1' is picked do
    if C == 1:
        print("You chose Prim's Algorithm!")
        print('')
        print("Prim's MST (Node to node: weight)-- ")
        print(printPrims(prim()))
        # prim()
        print("")
        print("You have returned to the main menu, please make another choice: ")
        menu()


    # If '2' is picked do
    elif C == 2:
        print("You chose Kruskal's Algorithm!")
        print('')
        print("Kruskal's MST (Node to node: weight)-- ")
        mst_kruskal = graph.kruskal()
        kruskal_print(mst_kruskal)
        print('')
        print("You have returned to the main menu, please make another choice: ")
        menu()

    # If '3' is picked do
    elif C == 3:
        print("You chose Prim's Shortest Path! For nodes enter integers 1-10")
        primsStart = int(input("Start Node: "))
        primsEnd = int(input("End Node: "))
        mst_prim = graph_generator((prim()))
        print("Prim's Shortest Path: ")
        print(mst_prim.path_finder(primsStart, primsEnd))
        print("You have returned to the main menu, please make another choice: ")
        menu()

    # If '4' is
    elif C == 4:
        print("You chose Kruskal's Shortest Path! For nodes enter integers 1-10")
        krusStart = int(input("Start Node: "))
        krusEnd = int(input("End Node: "))

        print("Kruskal's Shortest Path: ")
        mst_kruskal = graph.kruskal()
        print(mst_kruskal.path_finder(krusStart, krusEnd))
        print("You have returned to the main menu, please make another choice: ")
        menu()

    # If '5' is picked do
    elif C == 5:
        print("You chose to see the time efficiencies of Prims and Kruskals!")
        print("Prim's time: ")
        print("Time: {:.6f} seconds.".format(primTime()))
        print('')
        print("Kruskal's Time: ")
        print("Time: {:.6f} seconds.".format(kruskalTime()))
        print('')

        print("You have returned to the main menu, please make another choice: ")
        menu()


    # If '6' is picked do
    elif C == 6:
        TSPmenu()

    # If '7' is picked
    elif C == 7:
        exit

    # If the user enters something wrong go back to the menu
    else:
        print('Invalid. Try again')
        menu()


# --------------------------------END MAIN MEN-----------------------------------

# ----------------------------------TSP MENU-------------------------------------
# Global variables
cc2 = [[0, 2, 9, float("inf")], [1, 0, 6, 4], [float("inf"), 7, 0, 8], [6, 3, float("inf"), 0]]  # City Circuit 2
cc3 = [[0, 14, 4, 10, 20], [14, 0, 7, 8, 7], [4, 5, 0, 7, 16], [11, 7, 9, 0, 2], [18, 7, 17, 4, 0]]  # City Circuit 3
start_path = []


# TSPmenu loops the program and allows theuser to decide what city circuit to test
def TSPmenu():
    start_path[:] = []  # set start_path to default
    print("\n***Welcome to the Traveling Salesman Problem!***")
    print("To run the code on City Circuit 2, input '2'. To test City Circuit 3, input '3'.")
    userInput = input()
    time0 = time.clock()  # sets the time
    # Determines which city circuit to test based on user's input
    if (userInput == "2"):
        print("\n***City Circuit 2***")
        tsp(cc2)
        time1 = time.clock()
        print("    -Time:")
        print("\t{:.6f} seconds.".format(time1 - time0))
        print('')
        print("You are now back to the main menu")
        menu()
    elif (userInput == "3"):
        print("\n***City Circuit 3***")
        tsp(cc3)
        time1 = time.clock()
        print("    -Time:")
        print("\t{:.6f} seconds.".format(time1 - time0))
        print('')
        print("You are now back to the main menu")
        menu()
    else:
        print("\nInvalid input, try again.")
        TSPmenu()


# ---------------------------------END TSP MENU----------------------------------








# ----------------------------Prim & Kruskal Algorithms--------------------------

# Helps with the pathfinding of the MST's
# Graph class
class Graph(object):
    def __init__(self):
        self.data = {}

    # Adds nodes and links the weight of the edges both ways e.g: (1,2) and (2,1)
    def add(self, v1, v2, weight):
        if v1 not in self.data:
            self.data[v1] = {}

        if v2 not in self.data:
            self.data[v2] = {}

        self.data[v1][v2] = weight
        self.data[v2][v1] = weight

    # Checks to see if any two nodes have edges
    def has_edge(self, v1, v2):
        return v2 in self[v1] or v1 in self[v2]

    # Returns a list of all the edges in the graph
    def edges(self):
        data = []

        for src, destinations in self.data.items():
            for dest, weight in destinations.items():
                if (dest, src, weight) not in data:
                    data.append((src, dest, weight))

        return data

    # Sorts edges by their weight
    def sorted_by_weight(self):
        return sorted(self.edges(), key=lambda x: x[2])

    #          KRUSKAL'S ALGORITHM

    # Creates a Graph object for the Minimum Spanning Tree
    def kruskal(self):
        mst = Graph()
        parent = {}
        height = {}

        # Searches for the parent
        def find_parent(v):
            while parent[v] != v:
                v = parent[v]

            return v

        # Creates a union between roots by using parent and height relationship introduced in class
        def union(root1, root2):
            if height[root1] > height[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1

                if height[root2] == height[root1]:
                    height[root2] += 1

        # Implements the create-set structure introduced in class
        for v in self.data:
            parent[v] = v
            height[v] = 0

        # Sorts the edges and removes the unnecessary ones for the MST
        for v1, v2, weight in self.sorted_by_weight():
            parent1 = find_parent(v1)
            parent2 = find_parent(v2)

            if parent1 != parent2:
                mst.add(v1, v2, weight)
                union(parent1, parent2)

            if len(self) == len(mst):
                break

        return mst

    #         END OF KRUSKAL'S




    # Helpers for Prims
    # Computes the length of the graph by receiving all the keys of the hashmaps created in {node: destination} pattern
    def __len__(self):
        return len(self.data.keys())

    # A getter for the potential destinations the node can get to
    def __getitem__(self, node):
        return self.data[node]

    def __iter__(self):
        for edge in self.edges():
            yield edge

    def __str__(self):
        return "\n".join('From v%s to v%s: %d' % edge for edge in self.edges())

    # Implements a recursive Depth-First Search Algorithm to trace the path
    def trace_path(self, start, end, path=None):

        # Converts the potential destinations of the selected node into a set for further calculations
        temp = set()
        for v in self.__getitem__(start):
            temp.add(v)

        # Starts with the given "start" point
        if path is None:
            path = [start]
        # Outputs the path if given "start" is the given "end"
        if start == end:
            yield path
        # Calls recursion to figure out the path
        for next in temp - set(path):
            yield from self.trace_path(next, end, path + [next])

    def path_sum(self, start, end):
        sum = 0
        lis = list(self.trace_path(start, end))

        for i in range(len(lis[0]) - 1):
            sum += self.data[lis[0][i]][lis[0][i + 1]]
        return sum

    def path_finder(self, start, end):
        a = "Shortest path: v" + str(start)
        lis = list(self.trace_path(start, end))
        for i in range(len(lis[0]) - 1):
            a = a + " -> v" + str(lis[0][i + 1])
        a = a + "\nWeight: " + str(self.path_sum(start, end))
        return a


# Initializes the graph
graph = Graph()
graph.add(1, 2, 32)
graph.add(1, 4, 17)
graph.add(2, 5, 45)
graph.add(3, 4, 18)
graph.add(3, 7, 5)
graph.add(4, 5, 10)
graph.add(4, 8, 3)
graph.add(5, 6, 28)
graph.add(5, 9, 25)
graph.add(6, 10, 6)
graph.add(7, 8, 59)
graph.add(8, 9, 4)
graph.add(9, 10, 12)


def graph_generator(inp):
    gr = Graph()
    for i in range(len(inp)):
        gr.add(inp[i][1], inp[i][2], inp[i][0])
    return gr


#This function allows for Kruskals graph to be printed in the order it is done
def kruskal_print(inp):
    b = inp.sorted_by_weight()
    for i in range(len(b)):
        result = "From v" + str(b[i][0]) + " to v" + str(b[i][1]) + ": " + str(b[i][2])
        print(result)

#       PRIM'S ALGORITHM

# each row represents an edge as follows: [weight, start, end]
edges = [[17, 1, 4], [32, 1, 2], [45, 2, 5], [10, 4, 5], [18, 3, 4],
         [5, 3, 7], [59, 7, 8], [3, 4, 8], [4, 8, 9], [25, 5, 9],
         [28, 5, 6], [6, 6, 10], [12, 9, 10]]


def val_exist(element, ls):
    if element in ls:
        return 1
    else:
        return 0


# returns a 2d list without rows
def rm_rows_with_vals(ls, vals):
    temp = []
    for i in range(0, len(ls)):
        if not (val_exist(ls[i][1], vals) or val_exist(ls[i][2], vals)):
            temp.append(ls[i])

    return temp


# returns a 2d list without rows of given index values
def rm_rows_with_indexes(ls, indexes):
    temp = []
    for i in range(0, len(ls)):
        if i not in indexes:
            temp.append(ls[i])

    return temp


# gets the index of an edge from the edge list
def get_edges_index(edges, ls):
    for i in range(0, len(edges)):
        if set(edges[i]) == set(ls):
            return i


# creates a list of all the nodes in the list of edges
def get_unique_nodes(edges):
    vals = []
    for i in edges:
        vals.append(i[1])
        vals.append(i[2])

    vals = set(vals)
    return vals


# implements prim's algorithm
def prim():
    edges = [[17, 1, 4], [32, 1, 2], [45, 2, 5], [10, 4, 5], [18, 3, 4], [5, 3, 7], [59, 7, 8], [3, 4, 8], [4, 8, 9],
             [25, 5, 9], [28, 5, 6], [6, 6, 10], [12, 9, 10]]

    mst = []
    active_list = []
    curr_nodes = [1]
    all_nodes = get_unique_nodes(edges)
    mod_edges = edges
    active_list_new = active_list

    while (len(curr_nodes) <= len(all_nodes) + 1):
        # search edges for selected nodes and add to active list
        for i in range(0, len(edges)):
            for j in range(0, len(curr_nodes)):
                if (edges[i][1] == curr_nodes[j] and edges[i][2] not in curr_nodes) or (
                        edges[i][2] == curr_nodes[j] and edges[i][1] not in curr_nodes):
                    active_list.append(edges[i])

        mod_edges = rm_rows_with_vals(mod_edges, curr_nodes)

        curr_min = float("inf")
        curr_min_index = -1
        # search active list for smallest weighted edge
        for i in range(0, len(active_list)):
            if curr_min > active_list[i][0]:
                curr_min = active_list[i][0]

        # look for curr_min's row and add that to mst and its brother node to curr_nodes
        for i in range(0, len(active_list)):
            if curr_min == active_list[i][0]:
                curr_min_index = i
                # only add if and only if one element is in curr_nodes and one element is not
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

    # print("MST: " + str(mst))
    return mst


# prim()


# This function will help print out prims in same setup as kruskals
def printPrims(MST):
    for i in range(len(MST)):
        print("From v", (MST[i][1]), " to v", (MST[i][2]), ": ", (MST[i][0]))
#End Prims








# Timers
def primTime():
    time0 = time.clock()  # initial prim time
    prim()
    time1 = time.clock()  # determines time
    primTime = time1 - time0
    return primTime


def kruskalTime():
    time0 = time.clock()  # initial prim time
    graph.kruskal()
    time1 = time.clock()  # determines time
    kruskalTime = time1 - time0
    return kruskalTime





# Added this code together in finalization step
''' Compile this code
#mst_kruskal = graph.kruskal()
#mst_prim = graph_generator(prim())
print("\n***Prim's Algorithm***")
print(mst_prim.path_finder(1, 6))
time0 = time.clock()    #initial prim time
prim()
time1 = time.clock()    #determines time
kruskalTime = time1 - time0
print("Time: {:.6f} seconds.".format(time1-time0))
print("\n")
print("***Kruskal's Algorithm***")
print(mst_kruskal.path_finder(1, 10))
time0 = time.clock()    #initial kruskal time
kruskal()
time1 = time.clock()    #determines time
primTime = time0 - time1
print("Time: {:.6f} seconds.".format(time1-time0))


'''

# ---------------------------------END PRIM&KRUSKAL------------------------------








# ---------------------------TSP Algorithm & Related Code------------------------
# Global variables
cc2 = [[0, 2, 9, float("inf")], [1, 0, 6, 4], [float("inf"), 7, 0, 8], [6, 3, float("inf"), 0]]  # City Circuit 2
cc3 = [[0, 14, 4, 10, 20], [14, 0, 7, 8, 7], [4, 5, 0, 7, 16], [11, 7, 9, 0, 2], [18, 7, 17, 4, 0]]  # City Circuit 3
start_path = []  # Salesman Graph


# removes an element of a list with given index
def rmel(ls, index):
    return ls[:index] + ls[index + 1:]


# solves subproblems of tsp
def subtsp(target, comp, matrix):
    if len(comp) == 1:
        # get the first 2 nodes touched by the salesman
        if len(start_path) < 3:
            start_path.append(target)

        return matrix[comp[0]][target] + matrix[0][comp[0]]


    elif len(comp) != 0:
        temp = float("inf")

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
    start_node = 0  # LET USER INPUT START NODE AND ADD ERROR CHECKING FOR CC1 AND CC2

    # Adds all nodes except for the start node to cities
    for i in range(0, len(matrix)):
        if i != start_node:
            cities.append(i)

    start_path.append(start_node)
    my_tsp = subtsp(start_node, cities, matrix)
    start_path.append(start_node)
    start_path_new = [x + 1 for x in start_path]
    print("    -Path: ")
    print("", *start_path_new, sep=' -> v')

    print("    -Weight:\n" + "\t" + str(my_tsp))

# -----------------------------------END TSP CODE---------------------------------

###################################END OF PROGRAM###############################


