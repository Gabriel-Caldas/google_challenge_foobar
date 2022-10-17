from collections import defaultdict
import time

# func to build the graph
def build_graph():
    # nodes conections (origin, destiny, weigth)
    edges = [['1', '2'], ['1', '6'], #+1/+5
             ['2', '3'], ['2', '7'], #+1/+5
             ['6', '7'], ['6', '11'],
             ['3', '4'], ['3', '8'],
             ['7', '8'], ['7', '12'],
             ['11', '12'], ['11', '16'], #+1/+5
             ['4', '5'], ['4', '9'],
             ['8', '7'], ['8', '9'], ['8', '3'], ['8', '13'],
             ['12', '11'], ['12', '13'], ['12', '7'], ['12', '17'],
             ['16', '17'], ['16', '21'],
             ['5', '10'],
             ['9', '8'], ['9', '10'], ['9', '4'], ['9', '14'],
             ['13', '12'], ['13', '14'], ['13', '8'], ['13', '18'],
             ['17', '16'], ['17', '18'], ['17', '12'], ['17', '22'],
             ['21', '22'], 
             ['10', '9'], ['10', '15'],
             ['14', '13'], ['14', '15'], ['14', '9'], ['14', '19'],
             ['18', '17'], ['18', '19'], ['18', '13'],['18', '23'],
             ['22', '23'], ['22', '17'], #+1/-5
             ['15', '14'], ['15', '20'],
             ['19', '18'], ['19', '20'], ['19', '14'], ['19', '24'],
             ['23', '24'], ['23', '18'],
             ['20', '25'],
             ['24', '25']]



    # graph as a defaultdict object
    graph = defaultdict(list)

    # create iteractions
    for edge in edges:
        # start and final nodes
        sn, fn = edge

        # create connections as undirect graph
        graph[sn].append(fn)
        # graph[fn].append(sn)

    return graph

weights = {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 1 ,
           '6' : 1, '7' : 0, '8' : 1, '9' : 0, '10' : 1,
           '11' : 1, '12' : 0, '13' : 1, '14' : 0, '15' : 1,
           '16' : 1, '17' : 0, '18' : 1, '19' : 0, '20' : 1,
           '21' : 1, '22' : 0, '23' : 0, '24' : 1, '25' : 0}

def weighted_nodes(curr_weight, nodes_list):
    for node in nodes_list:
        node[1] = node[1] + curr_weight
    
    return nodes_list

def path_length(graph, weights,start, end):
    path_len = 0
    curr_nodes = [[start, weights[start], path_len]]
    prev_nodes = [None]
    count = 0
    while True:
        nxt_nodes = []
        for curr_node in curr_nodes:
            # if input() == 'q':
            #     return 'end'
            # print(f"{curr_node}")#/{curr_nodes}")
            
            parent_node_id = curr_node[0]
            parent_weight = curr_node[1]
            parent_len = curr_node[2]
            for children_node in graph[parent_node_id]:
                parent_len += 1
                if end in children_node:
                    print('CHEGOU')
                    
                    return curr_nodes[0][2]
                path_weight = parent_weight+weights[children_node]
                if path_weight <= 1:
                    nxt_nodes.append([children_node, path_weight, parent_len])
        curr_nodes = nxt_nodes


graph = build_graph()
# print(graph)
t0 = time.time()
print(path_length(graph, weights, '1', '25'))
print(f"Tempo: {time.time() - t0}")
# BFS_SP(graph, 'A', 'D')