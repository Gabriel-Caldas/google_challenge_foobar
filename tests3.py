from collections import defaultdict
import itertools
import numpy as np


import time

def get_edges(maze):
    maze = np.array(maze)
    h = maze.shape[0]
    w = maze.shape[1]
    left_corner = w
    right_corner =  (h-1)*w+1 
    edges_list = []
    for i in range(1,h*w):
        if i == left_corner:
            edge = [[str(i), str(i+w)]]
        elif i == right_corner:
            edge = [[str(i), str(i+1)]]
        elif w > i >1:
            edge = [[str(i), str(i+1)], [str(i), str(i+w)]]
        elif i%w == 0 and i != w:
            edge = [[str(i), str(i-1)], [str(i), str(i+w)]]
        elif (i-1)%w == 0:
            edge = [[str(i), str(i+1)], [str(i), str(i+w)]]
        elif (h*w) > i > ((h-1)*w+1):
            edge = [[str(i), str(i+1)], [str(i), str(i-w)]]
        else:
            edge = [[str(i), str(i-1)], [str(i), str(i+1)], [str(i), str(i-w)], [str(i), str(i+w)] ]
        edges_list.extend(edge)
    
    return edges_list

def get_weights(maze):
    weights = {}
    maze = np.array(maze)
    maze_T = maze.reshape(1, -1)[0]
    for i, weight in enumerate(maze_T):
        weights[str(i+1)] = weight
    
    return weights

# func to build the graph
def build_graph(edges_list):
    # nodes conections (origin, destiny, weigth)
    edges = edges_list

    # graph as a defaultdict object
    graph = defaultdict(list)

    # create iteractions
    for edge in edges:
        # start and final nodes
        sn, fn = edge

        graph[sn].append(fn)

    return graph



def solution(maze):
    edges_list = get_edges(maze)
    weights = get_weights(maze)
    graph = build_graph(edges_list)
    start = str(1)
    end = str(len(maze) * len(maze[0]))

    # graph, weights,start, end):
    path_len = 1
    curr_nodes = [[start, weights[start], path_len]]
    parent_len = 0
    while True:
        nxt_nodes = []
        for curr_node in curr_nodes:
            parent_node_id = curr_node[0]
            parent_weight = curr_node[1]
            parent_len = curr_node[2]
            parent_len += 1
            if end in graph[parent_node_id]:
                return parent_len
            for children_node in graph[parent_node_id]:
                path_weight = parent_weight+weights[children_node]
                if path_weight <= 1:
                    nxt_nodes.append([children_node, path_weight, parent_len])
        nxt_nodes.sort()
        curr_nodes = list(unique for unique, _ in itertools.groupby(nxt_nodes))





# maze = [[0, 1, 1, 0], 
#         [0, 0, 0, 1], 
#         [1, 1, 0, 0], 
#         [1, 1, 1, 0]]
# maze = [[0, 0, 0, 0, 0, 0], 
#         [1, 1, 1, 1, 1, 0], 
#         [0, 0, 0, 0, 0, 0], 
#         [0, 1, 1, 1, 1, 1], 
#         [0, 1, 1, 1, 1, 1], 
#         [0, 0, 0, 0, 0, 0]]

# edges_list = get_edges(maze)
# weights = get_weights(maze)
# graph = build_graph(edges_list)

# start = str(1)
# end = str(len(maze) * len(maze[0]))
# # print(graph)
# print(path_length(graph, weights, start, end))

t0 = time.time()
maze = np.zeros([40, 40])

print(solution(maze))
print(f"Tempo Total: {time.time() - t0}")