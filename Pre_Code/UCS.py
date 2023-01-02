import pandas as pd
import numpy as np
from queue import PriorityQueue
import time

def uniform_cost_search(goal, start):
    global graph,cost,path,matrix
    q = PriorityQueue()
    q.put([0, start, []])
    #the 1st element is the current cost
    #the 2nd element is the current node
    #the 3rd element is the path to current node
    visited = [] #mark by list

    while not q.empty():
        #p is the best node found
        p = q.get()

        if (p[1] == goal):
            path = p[2] + [goal]
            return p[0]
        
        if (p[1] not in visited):
            for i in range(len(matrix[p[1]])):
                if matrix[p[1]][i] != 0:
                    q.put([(p[0] + matrix[p[1]][i]), i, p[2]+[p[1]]])
        
        visited.append(p[1])
    return None

def decode(n): #cái này để chuyển số thành tên tp
    global name
    return str(name[n])

def encode(str): #chuyển tên tp thành số
    for i in range(len(name)):
        if name[i] == str:
            return i


if __name__ == '__main__':

#đổi cái path ở dưới đến file excel
    df = pd.read_excel(r"Data\Car_Driving.xlsx")
    name = matrix = np.array(df)[::,0] #slice như này để lấy luôn index làm list tên tp
    matrix = np.array(df)[::,1:] #slice như này để bỏ 1 dòng index
    
    #đoạn còn lại thì input mí run code thoy ^^
    while True:
        start = input('START?')
        goal = input('GOAL?')
        if (start in name) and (goal in name):
            break
    start_time = time.time()
    
    answer = uniform_cost_search(encode(goal),encode(start))
    if answer == None: #if dont have any solutions
        print('no solution')

    else:	
        print('minimum cost from {} to {} is {} and the total time is '.format(start,goal,answer))
        print('path :')
        for i in path:
            print(decode(i),end=' -> ')
print()
print('RUNNING TIME UCS SEARCH')
print("--- %s seconds ---" % (time.time() - start_time))