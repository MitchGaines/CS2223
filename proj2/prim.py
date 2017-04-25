## Prims Algorithm
# This code will run prims algorithm against graph one. The code uses a priority
# queue and a list of visited nodes to keep track of the place and values of
# the graph.

from Queue import PriorityQueue
#http://stackoverflow.com/questions/9289614/how-to-put-items-into-priority-queues
''' Pseudo code:
    primsAlgorithm(graph[][], startValue)
        pq = make PriorityQueue()
        for vertices=0 to lengthOfVertices:
            graph[v] = infinity
            visitedList[v] = false

        graph[start] = 0

        #Build Queue?
        while pq.isEmpty():
            get pq value of edges from start
            extraxt min edge from pq
            if vertex of extracted edge !visited:
                add to MST
            cuurent vertext = 

        while pq is empty():
            current vertex = pq.addMin()
            
            '''
class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item

def prim(edges):
    queue = MyPriorityQueue()
    queue.put('v1', 1)

    curr_edges = edges

    temp = []
    
    for y in range(0, len(curr_edges)):
        if curr_edges[y][1] == 'v1' or  curr_edges[y][2] == 'v1':
            temp.append(curr_edges[y])

    curr_min = temp[0][0]
    for i in range(0, len(temp)):   
        curr_min = min(curr_min, temp[i][0])
        
    for i in range(0, len(temp)):
        if temp[i][0] == curr_min:
            if temp[i][1] == 'v1':
                queue.put(temp[i][2], 1)
            elif temp[i][2] == 'v1':
                queue.put(temp[i][1], 1)



        


'''
def prim(graph, start):
    priQ = PriorityQueue()
    for v=0 in graph.qsize():
        graph[v] = 0
        visited[v] = 0

    graph[start] = 0
'''
    
