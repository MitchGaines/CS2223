weight = dict()
parent = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def create_set(node):
    parent[node] = node
    weight[node] = 0

def union(node1, node2):
    parent1 = find(node1)
    parent2 = find(node2)
    if parent1 != parent2:
        if weight[parent1] > weight[parent2]:
            parent[parent2] = parent1
        else:
            parent[parent1] = parent2
        if weight[parent1] == weight[parent2]:
            weight[parent2] += 1


def kruskal(graph):
    for node in graph['nodes']:
        create_set(node)

    mst = set()
    edges = list(graph['edges'])
    edges.sort()

    for edge in edges:
        weight, node1, node2 = edge
        if find(node1) != find(node2):
            union(node1, node2)
            mst.add(edge)

    return sorted(mst)


graph = {
    'nodes': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': set([
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (15, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F'),
    ])
}

print(kruskal(graph))