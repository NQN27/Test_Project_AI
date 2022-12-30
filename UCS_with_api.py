import pandas as pd
import numpy as np
from queue import PriorityQueue
import time
import requests
import json

def uniform_cost_search(goal, start):
    global graph,cost,path,matrix
    q = PriorityQueue()
    q.put([0, start, [],0])
    #the 1st element is the current cost
    #the 2nd element is the current node
    #the 3rd element is the path to current node
    #the 4th element is the time cost
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
                    key='N87KvQLlqZMH3Q6qSQ2NhCm7zfaNyCr3G1N8n2F6'
                    start=location[p[2]][0]
                    finish=location[i][0]
                    url = "https://rsapi.goong.io/DistanceMatrix?origins={}&destinations={}&vehicle=car&api_key={}".format(start,finish,key)

                    payload={}
                    headers = {}

                    response = requests.request("GET", url, headers=headers, data=payload)
                    data=json.loads(response.text)

                    dist=data['rows'][0]['elements'][0]['distance']['value']
                    truetime=data['rows'][0]['elements'][0]['duration']['value']
                    q.put([(p[0] + dist), i, p[2]+[p[1]],p[3]+truetime])
        
        visited.append(p[1])
    return 0,0

def decode(n): #cái này để chuyển số thành tên tp
    global name
    return str(name[n])

def encode(str): #chuyển tên tp thành số
    for i in range(len(name)):
        if name[i] == str:
            return i


if __name__ == '__main__':

#đổi cái path ở dưới đến file excel thì code mí chạy nha mấy pa
    df = pd.read_excel(r"C:\Users\FPTSHOP\Desktop\AI_project\A\Car_Driving.xlsx")
    dh = pd.read_excel(r'C:\Users\FPTSHOP\Desktop\AI_project\A\Air_Distance.xlsx')
    dl = pd.read_excel(r"C:\Users\FPTSHOP\Desktop\AI_project\A\Location.xlsx")
    name = matrix = np.array(df)[::,0] #slice như này để lấy luôn index làm list tên tp
    matrix = np.array(df)[::,1:] #slice như này để bỏ 1 dòng index
    location=np.array(dl)[1:,1:]
    
    #đoạn còn lại thì input mí run code thoy ^^
    while True:
        start = input('START?')
        goal = input('GOAL?')
        if (start in name) and (goal in name):
            break
    start_time = time.time()
    
    answer,times = uniform_cost_search(encode(goal),encode(start))
    if answer == None: #if dont have any solutions
        print('no solution')

    else:	
        print('minimum cost from {} to {} is {} and the total time is {}'.format(start,goal,answer,times))
        print('path :')
        for i in path:
            print(decode(i),end=' -> ')
print()
print('RUNNING TIME UCS SEARCH')
print("--- %s seconds ---" % (time.time() - start_time))