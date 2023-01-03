import pandas as pd
import numpy as np
from queue import PriorityQueue
import time

def A_star(goal, start):
    global path,matrix
    q = PriorityQueue()
    q.put([0,0, start, [],0])
    #the 1rd element is the calculate cost (Using to Choose place to open) 
    #the 2st element is the current cost
    #the 3nd element is the current node
    #the 4th element is the path to current node
    #the 5th element is the true time cost
    visited = [] #Place that had opened

    while not q.empty():
        #p is the best node found
        p = q.get()

        if (p[2] == goal):
            path = p[3] + [goal]
            return p[1],p[4]
        
        if (p[2] not in visited):
            for i in range(len(matrix[p[2]])):
                if matrix[p[2]][i] != 0:
                    q.put([p[1]+matrix[p[2]][i]+heuristic[p[2]][i],(p[1] + matrix[p[2]][i]), i, p[3]+[p[2]],p[4]+Timecost[p[2]][i]])
        
        visited.append(p[2])
    return 0,0

def decode(n): #cái này để chuyển số thành tên tp
    global name
    return str(name[n])

def encode(str): #chuyển tên tp thành số
    for i in range(len(name)):
        if name[i] == str:
            return i


if __name__ == '__main__':

#Input the path of data
    df = pd.read_excel(r'Data\Car_Driving.xlsx')
    dh = pd.read_excel(r'Data\Air_Distance1.xlsx')
    dt = pd.read_excel(r"Data\TimeTravel.xlsx")
    name = matrix = np.array(df)[::,0] #Get file name of City
    
    matrix = np.array(df)[::,1:] #Remove the index
    heuristic = np.array(dh)[::,1:]
    Timecost = np.array(dt)[::,1:]
    #đoạn còn lại thì input mí run code thoy ^^
    while True:
        start = input('START?')
        goal = input('GOAL?')
        if (start in name) and (goal in name):
            break
    start_time = time.time()
    
    answer,times = A_star(encode(goal),encode(start))
    if answer == 0: #if dont have any solutions
        print('no solution')

    else:	
        print('minimum cost from {} to {} is {} km and time cost is {} mins'.format(start,goal,answer,times))
        print('path :')
        for i in path:
            print(decode(i),end=' -> ')
print()
print('RUNNING TIME A*')
print("--- %s seconds ---" % (time.time() - start_time))