
import numpy as np

class Bunny:
    
    def __init__(self):
        self.position = [0,0]
        self.last_position = [0,0]

    def move_l(self):
        self.last_position = self.position.copy()
        self.position[1] = self.position[1] - 1
    def move_r(self):
        self.last_position = self.position.copy()
        self.position[1] = self.position[1] + 1
    def move_u(self):
        self.last_position = self.position.copy()
        self.position[0] = self.position[0] - 1
    def move_d(self):
        self.last_position = self.position.copy()
        self.position[0] = self.position[0] + 1

    def check_end(self, map):
        if self.position == [map.shape[0] -1, map.shape[1]-1]:
            return True
        return False

class Transformation():
    def __init__(self):
        self.done = False
    
    def transform(self):
        self.done = True


def left_allowed(map, i, j, bunny, transformation):
    if j - 1 >= 0:
        next = map[i, j-1]
        if bunny.last_position == [i, j-1]:
            return False
    else:
        return False
    if next == 1 and not transformation.done:
        return True
    elif next == 1:
        return False
    return True

def right_allowed(map, i, j, bunny, transformation):
    if j + 1 < map.shape[1]:
        next = map[i, j+1]
        if bunny.last_position == [i, j+1]:
            return False
    else:
        return False
    if next == 1 and not transformation.done:
        return True
    elif next == 1:
        return False
    return True

def up_allowed(map, i, j, bunny, transformation):
    if i - 1 >= 0:
        next = map[i - 1, j]
        if bunny.last_position == [i-1, j]:
            return False
    else:
        return False 
    if next == 1 and not transformation.done:
        return True
    elif next == 1:
        return False
    return True

def down_allowed(map, i, j, bunny, transformation):
    if i + 1 < map.shape[0]:
        next = map[i+1, j]
        if bunny.last_position == [i+1, j]:
            return False
    else:
        return False
    if next == 1 and not transformation.done:
        return True
    elif next == 1:
        return False
    return True

def dirs_allowed(map, i, j, bunny, transformation):
    i = i
    j = j
    l = left_allowed(map, i, j, bunny, transformation)
    r = right_allowed(map, i, j, bunny, transformation)
    u = up_allowed(map, i, j, bunny, transformation)
    d = down_allowed(map, i, j, bunny, transformation)
    directions = [l, r, u, d] #left, right, up, down

    return directions


# map = np.array([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]])
map =  np.array([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])

transformation = Transformation()
bunny = Bunny()
length = 0
while True:
    i = bunny.position[0]
    j = bunny.position[1]
    lp = bunny.last_position
    if map[i,j] == 1:
        transformation.transform()
    print(f"Position: {bunny.position} == {map[i,j]}, Last Position: {bunny.last_position} Transformed: {transformation.done}")
    print(dirs_allowed(map, i, j, bunny, transformation))
    command = int(input('Next Step: '))
    if command == 4:
        bunny.move_l()
    if command == 6:
        bunny.move_r()
    if command == 8:
        bunny.move_u()
    if command == 2:
        bunny.move_d()
    length +=1
    if bunny.check_end(map):
        print(f"Path length: {length}")
        print('THE END')
        break


