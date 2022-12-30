import pandas as pd
import numpy as np
from queue import PriorityQueue
import time

        
def A_star(goal, start,time_start):
    global path,matrix
    q = PriorityQueue()
    q.put([0,0, start, [],time_start])
    #the 1rd element is the calculate cost (Using to Choose place to open) 
    #the 2st element is the current cost
    #the 3nd element is the current node
    #the 4th element is the path to current node
    #the 5th element is the current time
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
                    q.put([p[1]+matrix[p[2]][i]+heuristic[goal][i],(p[1] + matrix[p[2]][i]), i, p[3]+[p[2]],p[4]+Total_time(Timecost[p[2]][i],Expand_Time[p[2]][i],p[4])])
        
        visited.append(p[2])
    return 0,0

def Total_time(Real_time,Expand_time,Current_time):
    # calculate true time cost
    if (Current_time > 600 and Current_time < 780) or (Current_time >1050  and Current_time <1170):
        return Real_time+Expand_time
    else:
        return Real_time
    
def decode(n): #cái này để chuyển số thành tên tp
    global name
    return str(name[n])

def encode(str): #chuyển tên tp thành số
    for i in range(len(name)):
        if name[i] == str:
            return i


if __name__ == '__main__':

#Input the path of data
    df = pd.read_excel(r"C:\Users\FPTSHOP\Desktop\AI_project\A\matrix.xlsx")
    dh = pd.read_excel(r'C:\Users\FPTSHOP\Desktop\AI_project\A\Air_Distance1.xlsx')
    dt = pd.read_excel(r"C:\Users\FPTSHOP\Desktop\AI_project\A\Real_Time.xlsx")
    dtx = pd.read_excel(r"C:\Users\FPTSHOP\Desktop\AI_project\A\Extra_Time.xlsx")
    name = np.array(dh)[::,0] #Get file name of City
    
    matrix = np.array(df)[::,1:]/1000 #Remove the index
    heuristic = np.array(dh)[::,1:]
    Timecost = np.array(dt)[::,1:]
    Expand_Time = np.array(dtx)[::,1:]
    #đoạn còn lại thì input mí run code thoy ^^

    while True:
        start = input('START?')
        goal = input('GOAL?')
        '''
        hour=int(input('Hour='))
        mins=int(input('Mins='))
        '''
        if (start in name) and (goal in name):
            '''and (hour>=0 and hour<24) and (mins>=0 and mins<60)'''
            break
    start_time = time.time()
    
    answer,times = A_star(encode(goal),encode(start),0)
    if answer == 0: #if dont have any solutions
        print('no solution')

    else:	
        print('minimum cost from {} to {} is {} km and arrive at {} hours {} mins'.format(start,goal,answer,times//60,times%60))
        print('path :')
        for i in path:
            print(decode(i),end=' -> ')
print()
print('RUNNING TIME A*')
print("--- %s seconds ---" % (time.time() - start_time))

            