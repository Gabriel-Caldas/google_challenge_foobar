from collections import defaultdict

# func to build the graph
def build_graph():
    # nodes conections (origin, destiny, weigth)
    edges = [['A', 'B', 0], ['A', 'E', 0], 
             ['A', 'C', 1], ['B', 'D', 1], 
             ['B', 'E', 0], ['C', 'F', 1],
             ['C', 'G', 1], ['D', 'E', 1],
             ['G', 'H', 0], ['H', 'I', 0],
             ['I', 'J', 0], ['I', 'K', 1] ]

    # graph as a defaultdict object
    graph = defaultdict(list)

    # create iteractions
    for edge in edges:
        # start and final nodes
        sn, fn = edge[0], edge[1]

        # create connections as undirect graph
        graph[sn].append([fn,edge[2]])
        # graph[fn].append(sn)

    return graph

# def path_length(graph, start, end):
    curr_nodes = start
    prev_nodes = [None]
    count = 0

    while True:
        count += 1
        nxt_nodes = []
        for node in curr_nodes:
            if node not in prev_nodes:
                nxt_nodes.extend(graph[node])
        print(nxt_nodes)
        for nxt_node in nxt_nodes:
            if end in graph[nxt_node]:
                if count > 1:
                    return count + 1
                else:
                    return count
        prev_nodes = curr_nodes
        curr_nodes = nxt_nodes


def path_length(graph, start, end):
    graph_test = graph.copy()
    curr_nodes = [start]
    prev_nodes = [None]
    count = 0
    weigth = 0
    while True:
        count += 1
        nxt_nodes = []
        for node in curr_nodes:
            if node not in prev_nodes:
                node_w = graph[node][1]
                nxt_nodes.extend(graph[node])
        print(nxt_nodes)
        for nxt_node in nxt_nodes:
            if end in graph[nxt_node]:
                if count > 1:
                    return count + 1
                else:
                    return count
        prev_nodes = curr_nodes
        curr_nodes = nxt_nodes

graph = build_graph()
print(graph)
# print(graph)
# print(path_length(graph, 'A', 'I'))
# BFS_SP(graph, 'A', 'D')