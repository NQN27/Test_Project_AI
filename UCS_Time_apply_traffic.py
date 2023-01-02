import pandas as pd
import numpy as np
from queue import PriorityQueue
import time
import datetime
def uniform_cost_search(goal, start,Time_start):
    global path,Time_cost
    q = PriorityQueue()
    q.put([Time_start, start, []])
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
            for i in range(len(Time_cost[p[1]])):
                if Time_cost[p[1]][i] != 0:
                    q.put([(p[0] + Total_time(Time_cost[p[1]][i],Extra_time[p[1]][i],p[0])), i, p[2]+[p[1]]])
        
        visited.append(p[1])
    return None

def decode(n): #cái này để chuyển số thành tên tp
    global name
    return str(name[n])

def encode(str): #chuyển tên tp thành số
    for i in range(len(name)):
        if name[i] == str:
            return i
def Total_time(RTC,ET,CT):
    # calculate true time cost
    # RT: Real time cost, ET : Extra time, CT : Current time

    for i in range(int(CT//3600),int((RTC+CT)//3600)):
        if  Time_label[i]:
            return RTC+ET
    
    return RTC

if __name__ == '__main__':

#đổi cái path ở dưới đến file excel
    dt = pd.read_excel(r"C:\Users\FPTSHOP\Desktop\AI_project\Test_Project_AI\TimeTravel.xlsx")
    dtx = pd.read_excel(r"C:\Users\FPTSHOP\Desktop\AI_project\Test_Project_AI\Extra_Time.xlsx")
    name = np.array(dt)[::,0] #slice như này để lấy luôn index làm list tên tp
    Time_cost = np.array(dt)[::,1:] #slice như này để bỏ 1 dòng index
    Extra_time = np.array(dtx)[::,1:]*60
    Time_label=[True if i not in [10,11,12,17,18,19,34,35,36,41,42,43,58,59,60,65,66,67] else False for i in range(0,71)]
    #đoạn còn lại thì input mí run code thoy ^^
    while True:
        start = input('START?')
        goal = input('GOAL?')
        if (start in name) and (goal in name):
            break
    start_time = time.time()
    # Get the start time of the current day in seconds
    today = datetime.datetime.today()
    start_of_day = datetime.datetime(today.year, today.month, today.day)
    start_of_day_in_seconds = time.mktime(start_of_day.timetuple())

    # Calculate the elapsed time in seconds
    elapsed_time_in_seconds = start_time - start_of_day_in_seconds
    answer = uniform_cost_search(encode(goal),encode(start),elapsed_time_in_seconds)
    if answer == None: #if dont have any solutions
        print('no solution')

    else:	
        answer = answer-elapsed_time_in_seconds
        hours = int(answer//3600)
        mins = int((answer - hours*60*60)//60)
        seconds = int(answer%60)
        print('minimum time cost from {} to {} is {} hours {} mins {} seconds  '.format(start,goal,hours,mins,seconds))
        print('path :')
        for i in path:
            print(decode(i),end=' -> ')
print()
print('RUNNING TIME UCS SEARCH')
print("--- %s seconds ---" % (time.time() - start_time))