import pandas as pd
import numpy as np
from queue import PriorityQueue
import time
import requests
import json

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
                    
                    q.put([p[1]+dist+heuristic[p[2]][i],(p[1] + dist), i, p[3]+[p[2]],p[4]+truetime])
        
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
    dh = pd.read_excel(r'Data\Air_Distance.xlsx') 
    dl = pd.read_excel(r"Data\Location.xlsx")
    name = matrix = np.array(df)[::,0] #Get file name of City
    matrix = np.array(df)[::,1:]
    location=np.array(dl)[::,1:] #Remove the index
    heuristic = np.array(dh)[::,1:]
    
   #đoạn còn lại thì input mí run code thoy ^^
    while True:
        start = input('START?')
        goal = input('GOAL?')
        hour=int(input('Hour='))
        mins=int(input('Mins='))
        if (start in name) and (goal in name) and (hour>=0 and hour<24) and (mins>=0 and mins<60):
            break
    start_time = time.time()
    
    answer,times = A_star(encode(goal),encode(start),hour*60*60+mins*60)
    if answer == 0: #if dont have any solutions
        print('no solution')

    else:	
        print('minimum cost from {} to {} is {} km {} m and arrive at {} hours {} mins'.format(start,goal,answer//1000,answer%1000,times//3600,(times//60)%60))
        print('path :')
        for i in path:
            print(decode(i),end=' -> ')
print()
print('RUNNING TIME A*')
print("--- %s seconds ---" % (time.time() - start_time))
