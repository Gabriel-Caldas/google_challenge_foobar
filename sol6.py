"""
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.


"""
import time

from collections import defaultdict
import itertools
import numpy as np


def get_edges(map):
    """Takes map and returns list of links for each origin node (first node = 1)"""
    map = np.array(map)
    h = map.shape[0]
    w = map.shape[1]
    left_corner = w
    right_corner =  (h-1)*w+1 
    edges_list = []
    # loop of conection conditions for each kind of node 
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

def get_weights(map):
    """Takes map as matrix and returns each node weight"""
    weights = {}
    map = np.array(map)
    maze_T = map.reshape(1, -1)[0]
    for i, weight in enumerate(maze_T):
        weights[str(i+1)] = weight
    
    return weights

# func to build the graph
def build_graph(edges_list):
    """Takes nodes links list and returns the graph table without the weights"""
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

def solution(map):
    """Takes map and returns the length of the shortest allowed path from map[0][0] to map[h-1][w-1]"""
    edges_list = get_edges(map)
    weights = get_weights(map)
    graph = build_graph(edges_list)
    start = str(1) #start point 
    end = str(len(map) * len(map[0])) #end point (w-1, h-1)

    path_len = 1
    curr_nodes = [[start, weights[start], path_len]] # node info through path
    parent_len = 0
    while True:
        nxt_nodes = []
        for curr_node in curr_nodes:
            parent_node_id = curr_node[0]
            parent_weight = curr_node[1]
            parent_len = curr_node[2]
            parent_len += 1
            if end in graph[parent_node_id]: # reached the end
                return parent_len
            for children_node in graph[parent_node_id]:
                path_weight = parent_weight+weights[children_node]
                if path_weight <= 1: # can have one '1' through my way 
                    nxt_nodes.append([children_node, path_weight, parent_len])
        nxt_nodes.sort()
        curr_nodes = list(unique for unique, _ in itertools.groupby(nxt_nodes)) # same point at same weight are the same for the purpose





# map = [[0, 1, 1, 0], 
#         [0, 0, 0, 1], 
#         [1, 1, 0, 0], 
#         [1, 1, 1, 0]]
# map = [[0, 0, 0, 0, 0, 0], 
#         [1, 1, 1, 1, 1, 0], 
#         [0, 0, 0, 0, 0, 0], 
#         [0, 1, 1, 1, 1, 1], 
#         [0, 1, 1, 1, 1, 1], 
#         [0, 0, 0, 0, 0, 0]]

# edges_list = get_edges(map)
# weights = get_weights(map)
# graph = build_graph(edges_list)

# start = str(1)
# end = str(len(map) * len(map[0]))
# # print(graph)
# print(path_length(graph, weights, start, end))

t0 = time.time()
map = np.zeros([20, 20])

print(solution(map))
print(f"Tempo Total: {time.time() - t0}")