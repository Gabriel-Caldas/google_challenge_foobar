# h = 2
# w = 2
# left_corner = w
# right_corner =  (h-1)*w+1 
# for i in range(1,h*w):
#     if i == left_corner:
#         print(f"['{i}','{i+w}'],")
#     elif i == right_corner:
#         print(f"['{i}','{i+1}'],")

#     elif w > i >1:
#         print(f"['{i}', '{i+1}'], ['{i}','{i+w}'],")

#     elif i%w == 0 and i != w:
#         print(f"['{i}', '{i-1}'], ['{i}','{i+w}'],")
#     elif (i-1)%w == 0:
#         print(f"['{i}', '{i+1}'], ['{i}','{i+w}'],")
#     elif (h*w) > i > ((h-1)*w+1):
#         print(f"['{i}', '{i+1}'], ['{i}','{i-w}'],")
#     else:
#         print(f"['{i}', '{i-1}'], ['{i}','{i+1}'], ['{i}','{i-w}'], ['{i}','{i+w}'],")
    

    

#AUTO
# edges_list = [['1', '2'], ['1','6'],
# ['2', '3'], ['2','7'],
# ['3', '4'], ['3','8'],
# ['4', '5'], ['4','9'],
# ['5','10'],
# ['6', '7'], ['6','11'],
# ['7', '6'], ['7','8'], ['7','2'], ['7','12'],
# ['8', '7'], ['8','9'], ['8','3'], ['8','13'],
# ['9', '8'], ['9','10'], ['9','4'], ['9','14'],
# ['10', '9'], ['10','15'],
# ['11', '12'], ['11','16'],
# ['12', '11'], ['12','13'], ['12','7'], ['12','17'],
# ['13', '12'], ['13','14'], ['13','8'], ['13','18'],
# ['14', '13'], ['14','15'], ['14','9'], ['14','19'],
# ['15', '14'], ['15','20'],
# ['16', '17'], ['16','21'],
# ['17', '16'], ['17','18'], ['17','12'], ['17','22'],
# ['18', '17'], ['18','19'], ['18','13'], ['18','23'],
# ['19', '18'], ['19','20'], ['19','14'], ['19','24'],
# ['20', '19'], ['20','25'],
# ['21','22'],
# ['22', '23'], ['22','17'],
# ['23', '24'], ['23','18'],
# ['24', '25'], ['24','19'],]




# test
# edges_list = [['1', '2'], ['1', '6'], #+1/+5 $

#              ['2', '3'], ['2', '7'], #+1/+5 $
#              ['3', '4'], ['3', '8'], #+1/+5
#              ['4', '5'], ['4', '9'], #+1/+5
#              ['5', '10'], 
#              ['6', '7'], ['6', '11'], #+1/+5
#              ['7', '8'], ['7', '12'], #+1/+5
#              ['8', '7'], ['8', '9'], ['8', '3'], ['8', '13'],
#              ['9', '8'], ['9', '10'], ['9', '4'], ['9', '14'],
#              ['10', '9'], ['10', '15'],
#              ['11', '12'], ['11', '16'], #+1/+5
#              ['12', '11'], ['12', '13'], ['12', '7'], ['12', '17'],
#              ['13', '12'], ['13', '14'], ['13', '8'], ['13', '18'],
#              ['14', '13'], ['14', '15'], ['14', '9'], ['14', '19'],
#              ['15', '14'], ['15', '20'],
#              ['16', '17'], ['16', '21'], #+1/+5
#              ['17', '16'], ['17', '18'], ['17', '12'], ['17', '22'],
#              ['18', '17'], ['18', '19'], ['18', '13'],['18', '23'],
#              ['19', '18'], ['19', '20'], ['19', '14'], ['19', '24'],
#              ['20', '25'],
#              ['21', '22'], 
#              ['22', '23'], ['22', '17'], #+1/-5
#              ['23', '24'], ['23', '18'],
#              ['24', '25']]


# weights = {'1' : 0, '2' : 1, '3' : 1, '4' : 1, '5' : 1 ,
#            '6' : 0, '7' : 1, '8' : 0, '9' : 0, '10' : 0,
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

# auto edges
# edges_list = [['1', '2'], ['1','5'],
# ['2', '3'], ['2','6'],
# ['3', '4'], ['3','7'],
# ['4','8'],
# ['5', '6'], ['5','9'],
# ['6', '5'], ['6','7'], ['6','2'], ['6','10'],
# ['7', '6'], ['7','8'], ['7','3'], ['7','11'],
# ['8', '7'], ['8','12'],
# ['9', '10'], ['9','13'],
# ['10', '9'], ['10','11'], ['10','6'], ['10','14'],
# ['11', '10'], ['11','12'], ['11','7'], ['11','15'],
# ['12', '11'], ['12','16'],
# ['13','14'],
# ['14', '15'], ['14','10'],
# ['15', '16'], ['15','11'],]

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

# weights = {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0 , '6' : 0, 
#            '7' : 1, '8' : 1, '9' : 1, '10' : 1, '11' : 1, '12' : 0, 
#            '13' : 0, '14' : 0, '15' : 0, '16' : 0, '17' : 0, '18' : 0, 
#            '19' : 0, '20' : 1, '21' : 1, '22' : 1, '23' : 1, '24' : 1, 
#            '25' : 0, '26' : 1, '27' : 1, '28' : 1, '29' : 1, '30' : 1,
#            '31' : 0, '32': 0, '33' : 0, '34' : 0, '35' : 0, '36' : 0}

#AUTO
# edges_list = [['1', '2'], ['1','7'],
# ['2', '3'], ['2','8'],
# ['3', '4'], ['3','9'],
# ['4', '5'], ['4','10'],
# ['5', '6'], ['5','11'],
# ['6','12'],
# ['7', '8'], ['7','13'],
# ['8', '7'], ['8','9'], ['8','2'], ['8','14'],
# ['9', '8'], ['9','10'], ['9','3'], ['9','15'],
# ['10', '9'], ['10','11'], ['10','4'], ['10','16'],
# ['11', '10'], ['11','12'], ['11','5'], ['11','17'],
# ['12', '11'], ['12','18'],
# ['13', '14'], ['13','19'],
# ['14', '13'], ['14','15'], ['14','8'], ['14','20'],
# ['15', '14'], ['15','16'], ['15','9'], ['15','21'],
# ['16', '15'], ['16','17'], ['16','10'], ['16','22'],
# ['17', '16'], ['17','18'], ['17','11'], ['17','23'],
# ['18', '17'], ['18','24'],
# ['19', '20'], ['19','25'],
# ['20', '19'], ['20','21'], ['20','14'], ['20','26'],
# ['21', '20'], ['21','22'], ['21','15'], ['21','27'],
# ['22', '21'], ['22','23'], ['22','16'], ['22','28'],
# ['23', '22'], ['23','24'], ['23','17'], ['23','29'],
# ['24', '23'], ['24','30'],
# ['25', '26'], ['25','31'],
# ['26', '25'], ['26','27'], ['26','20'], ['26','32'],
# ['27', '26'], ['27','28'], ['27','21'], ['27','33'],
# ['28', '27'], ['28','29'], ['28','22'], ['28','34'],
# ['29', '28'], ['29','30'], ['29','23'], ['29','35'],
# ['30', '29'], ['30','36'],
# ['31','32'],
# ['32', '33'], ['32','26'],
# ['33', '34'], ['33','27'],
# ['34', '35'], ['34','28'],
# ['35', '36'], ['35','29'],]  



def get_edges(h, w):
    left_corner = w
    right_corner =  (h-1)*w+1 
    edges_list = []
    for i in range(1,h*w):
        if i == left_corner:
            # edge = [[str(i), str(i+w)]]
            print(f"['{i}','{i+w}'],")
        elif i == right_corner:
            # edge = [[str(i), str(i+1)]]
            print(f"['{i}','{i+1}'],")
        elif w > i >1:
            # edge = [[str(i), str(i+1)], [str(i), str(i+w)]]
            print(f"['{i}', '{i+1}'], ['{i}','{i+w}'],")
        elif i%w == 0 and i != w:
            # edge = [[str(i), str(i-1)], [str(i), str(i+w)]]
            print(f"['{i}', '{i-1}'], ['{i}','{i+w}'],")
        elif (i-1)%w == 0:
            # edge = [[str(i), str(i+1)], [str(i), str(i+w)]]
            print(f"['{i}', '{i+1}'], ['{i}','{i+w}'],")
        elif (h*w) > i > ((h-1)*w+1):
            # edge = [[str(i), str(i+1)], [str(i), str(i-w)]]
            print(f"['{i}', '{i+1}'], ['{i}','{i-w}'],")
        else:
            # edge = [[str(i), str(i-1)], [str(i), str(i+1)], [str(i), str(i-w)], [str(i), str(i+w)] ]
            print(f"['{i}', '{i-1}'], ['{i}','{i+1}'], ['{i}','{i-w}'], ['{i}','{i+w}'],")
        # edges_list.extend(edge)
    
    return edges_list

print(get_edges(5,5))