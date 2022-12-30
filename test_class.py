import pandas as pd
import numpy as np
from queue import PriorityQueue
import time

class city(object):
    def __init__(self, id, using_time = False, using_ucs = True):
        self.id = id
        self.name = decode(id)
        
        self.ucs_cost = None
        self.a_star_cost = None
        self.ucs_time = None
        self.a_star_time = None
        self.path = []
        
        self.using_time = using_time
        self.using_ucs = using_ucs
    
    def __eq__(self, other):
        if self.using_ucs == True: # using ucs
            if self.using_time == False: # consider cost only
                return self.ucs_cost == other.ucs_cost 
            return self.ucs_time == other.ucs_time #consider time only
        else: # using a*
            if  self.using_time == False:
                return self.a_star_cost == other.a_star_cost
            return self.a_star_time == other.a_star_time

    def __lt__(self, other):
        if self.using_ucs == True: # using ucs
            if self.using_time == False: # consider cost only
                return self.ucs_cost < other.ucs_cost 
            return self.ucs_time < other.ucs_time #consider time only
        else: # using a*
            if  self.using_time == False:
                return self.a_star_cost < other.a_star_cost
            return self.a_star_time < other.a_star_time
    
    def __le__(self, other):
        if self.using_ucs == True: # using ucs
            if self.using_time == False: # consider cost only
                return self.ucs_cost <= other.ucs_cost 
            return self.ucs_time <= other.ucs_time #consider time only
        else: # using a*
            if  self.using_time == False:
                return self.a_star_cost <= other.a_star_cost
            return self.a_star_time <= other.a_star_time
    
    def __gt__(self, other):
        if self.using_ucs == True: # using ucs
            if self.using_time == False: # consider cost only
                return self.ucs_cost > other.ucs_cost 
            return self.ucs_time > other.ucs_time #consider time only
        else: # using a*
            if  self.using_time == False:
                return self.a_star_cost > other.a_star_cost
            return self.a_star_time > other.a_star_time

    def __ge__(self, other):
        if self.using_ucs == True: # using ucs
            if self.using_time == False: # consider cost only
                return self.ucs_cost >= other.ucs_cost 
            return self.ucs_time >= other.ucs_time #consider time only
        else: # using a*
            if  self.using_time == False:
                return self.a_star_cost >= other.a_star_cost
            return self.a_star_time >= other.a_star_time

    def adjacent_city(self):
        adjacent = []
        for i in range(len(matrix[self.id])):
                if matrix[self.id][i] != 0:
                    adjacent.append(i)
        return adjacent

def uniform_cost_search(goal, start):
    global matrix
    q = PriorityQueue()
    
    p = city(start)
    p.ucs_cost = 0

    q.put(p)
    visited = [] #mark by list

    while not q.empty():
        #p is the best node found
        p = q.get()

        if (p.id == goal):
            path = p.path + [p.name]
            return p.ucs_cost, path
        
        if (p.name not in visited):
            for c in p.adjacent_city():
                p1 = city(c)
                p1.ucs_cost = p.ucs_cost + matrix[p.id][c]
                p1.path = p.path + [p.name]
                q.put(p1)
        
        visited.append(p.name)
    return None

def A_star_search(goal, start):
    q = PriorityQueue()
    p = city(start, False, False)
    p.ucs_cost = 0
    p.a_star_cost = 0

    q.put(p)
    visited = [] 

    while not q.empty():
        #p is the best node found
        p = q.get()

        if (p.id == goal):
            return p.ucs_cost, p.path + [p.name]
                
        if (p.name not in visited):
            for c in p.adjacent_city():
                p1 = city(c, False, False)
                p1.ucs_cost = p.ucs_cost + matrix[p.id][c]
                p1.a_star_cost = p1.ucs_cost + heuristic[p1.id][goal]
                p1.path = p.path + [p.name]
                q.put(p1)

        visited.append(p.name)
    return None


def decode(n): 
    global name
    return str(name[n])

def encode(str):
    for i in range(len(name)):
        if name[i] == str:
            return i


if __name__ == '__main__':
    df = pd.read_excel('/Users/luong/OneDrive - Hanoi University of Science and Technology/project/DRIVE.xlsx')
    df2 = pd.read_excel('/Users/luong/OneDrive - Hanoi University of Science and Technology/project/AIR.xlsx')
    heuristic = np.array(df2)[::,1:]
    name = np.array(df)[::,0] 
    matrix = np.array(df)[::,1:] 

    while True:
        start = input('START?')
        goal = input('GOAL?')
        if (start in name) and (goal in name):
            break
    t1 = time.time()
    answer = uniform_cost_search(encode(goal),encode(start))
    t2 = time.time()
    answer_a = A_star_search(encode(goal), encode(start))
    t3 = time.time()
    if answer == None: #if dont have any solutions
        print('no solution')

    else:	
        solution = answer[0]
        path = answer[1]
        print('ucs minimum cost from {} to {} is {}'.format(start,goal,solution))
        print('path :')
        for i in path:
            print(i, end='->')
        print('RUNNING TIME UCS SEARCH')
        print("--- %s seconds ---" % (t2 - t1))
    print()
    
    if answer_a == None: #if dont have any solutions
        print('no solution')

    else:	
        solution = answer_a[0]
        path = answer_a[1]
        print('a* minimum cost from {} to {} is {}'.format(start,goal,solution))
        print('path :')
        for i in path:
            print(i, end='->')        
        print('RUNNING TIME A* SEARCH')
        print("--- %s seconds ---" % (t3 - t2))
print()
