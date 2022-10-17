from collections import defaultdict
import time

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

        # create connections as undirect graph
        graph[sn].append(fn)
        # graph[fn].append(sn)

    return graph

# test
# edges_list = [['1', '2'], ['1', '6'], #+1/+5
#              ['2', '3'], ['2', '7'], #+1/+5
#              ['6', '7'], ['6', '11'],
#              ['3', '4'], ['3', '8'],
#              ['7', '8'], ['7', '12'],
#              ['11', '12'], ['11', '16'], #+1/+5
#              ['4', '5'], ['4', '9'],
#              ['8', '7'], ['8', '9'], ['8', '3'], ['8', '13'],
#              ['12', '11'], ['12', '13'], ['12', '7'], ['12', '17'],
#              ['16', '17'], ['16', '21'],
#              ['5', '10'],
#              ['9', '8'], ['9', '10'], ['9', '4'], ['9', '14'],
#              ['13', '12'], ['13', '14'], ['13', '8'], ['13', '18'],
#              ['17', '16'], ['17', '18'], ['17', '12'], ['17', '22'],
#              ['21', '22'], 
#              ['10', '9'], ['10', '15'],
#              ['14', '13'], ['14', '15'], ['14', '9'], ['14', '19'],
#              ['18', '17'], ['18', '19'], ['18', '13'],['18', '23'],
#              ['22', '23'], ['22', '17'], #+1/-5
#              ['15', '14'], ['15', '20'],
#              ['19', '18'], ['19', '20'], ['19', '14'], ['19', '24'],
#              ['23', '24'], ['23', '18'],
#              ['20', '25'],
#              ['24', '25']]

# weights = {'1' : 0, '2' : 1, '3' : 1, '4' : 1, '5' : 1 ,
#            '6' : 1, '7' : 1, '8' : 0, '9' : 0, '10' : 0,
#            '11' : 0, '12' : 1, '13' : 0, '14' : 1, '15' : 0,
#            '16' : 0, '17' : 1, '18' : 0, '19' : 1, '20' : 0,
#            '21' : 0, '22' : 0, '23' : 0, '24' : 1, '25' : 0}

# [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# edges_list = [['1', '2'], ['1', '5'], #+1/+h
#              ['2', '3'], ['2', '6'], #+1/+4
#              ['5', '6'], ['5', '9'],
#              ['3', '4'], ['3', '7'],
#              ['6', '7'], ['6', '10'],
#              ['9', '10'], ['9', '13'], #+1/+h
#              ['4', '8'], 
#              ['7', '6'], ['7', '8'], ['7', '3'], ['7', '11'],
#              ['10', '9'], ['10', '11'], ['10', '6'], ['10', '14'],
#              ['13', '14'],
#              ['8', '7'], ['8', '12'], 
#              ['11', '12'], ['11', '15'],
#              ['14', '15'], ['14', '10'],
#              ['12', '16'],
#              ['15', '16']]

# weights = {'1' : 0, '2' : 1, '3' : 1, '4' : 0, 
#            '5' : 0 , '6' : 0, '7' : 0, '8' : 1, 
#            '9' : 1, '10' : 1, '11' : 0, '12' : 0, 
#            '13' : 1, '14' : 1, '15' : 1, '16' : 0}

# [[0, 0, 0, 0, 0, 0], 
#  [1, 1, 1, 1, 1, 0], 
#  [0, 0, 0, 0, 0, 0], 
#  [0, 1, 1, 1, 1, 1], 
#  [0, 1, 1, 1, 1, 1], 
#  [0, 0, 0, 0, 0, 0]]

weights = {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0 , '6' : 0, 
           '7' : 1, '8' : 1, '9' : 1, '10' : 1, '11' : 1, '12' : 0, 
           '13' : 0, '14' : 0, '15' : 0, '16' : 0, '17' : 0, '18' : 0, 
           '19' : 0, '20' : 1, '21' : 1, '22' : 1, '23' : 1, '24' : 1, 
           '25' : 0, '26' : 1, '27' : 1, '28' : 1, '29' : 1, '30' : 1,
           '31' : 0, '32': 0, '33' : 0, '34' : 0, '35' : 0, '36' : 0}







def weighted_nodes(curr_weight, nodes_list):
    for node in nodes_list:
        node[1] = node[1] + curr_weight
    
    return nodes_list

def path_length(graph, weights,start, end):
    path_len = 1
    curr_nodes = [[start, weights[start], path_len]]
    parent_len = 0
    prev_nodes = [None]
    count = 0
    while True:
        nxt_nodes = []
        for curr_node in curr_nodes:
            # if input() == 'q':
                # return 'end'
            # print(f"{curr_node}/{curr_nodes}")
            
            parent_node_id = curr_node[0]
            parent_weight = curr_node[1]
            parent_len = curr_node[2]
            parent_len += 1
            for children_node in graph[parent_node_id]:
                # parent_len +=1 
                if end in children_node:

                    print('CHEGOU!')
                    # print(parent_len)
                    # print(graph[parent_node_id])
                    return parent_len 
                path_weight = parent_weight+weights[children_node]
                if path_weight <= 1:
                    nxt_nodes.append([children_node, path_weight, parent_len])
        curr_nodes = nxt_nodes


graph = build_graph(edges_list)
# print(graph)
t0 = time.time()
print(path_length(graph, weights, '1', '16'))
print(f"Tempo: {time.time() - t0}")
# BFS_SP(graph, 'A', 'D')