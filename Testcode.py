from Calculate_Air import haversine,location
import test_class
import requests
import json
from test_class import encode
from Calculate_RealDistance import transform,locations
from Code_interface import *
matrix = test_class.matrix
name = test_class.name

point,start,end = clicked()
#đoạn dưới chưa fix 

def transform_place_to_cordinate(place):
    key='N87KvQLlqZMH3Q6qSQ2NhCm7zfaNyCr3G1N8n2F6'
    url = "https://rsapi.goong.io/geocode?address={}&api_key={}".format(place,key)

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data=json.loads(response.text)
    lat=data['results'][0]['geometry']['location']['lat']
    lng=data['results'][0]['geometry']['location']['lng']
    return [lat,lng]

start_place=[21.0042694,105.8459098]
end_place=[10.400045751017585, 106.25207711047737]

def get_place(place):
    Chosen_place=[]
    for i in range(len(name)):
            p=str(location[i][0]).split(',')
            dis=haversine(place[0],place[1],float(p[0]),float(p[1]))
            if dis<=50:
                Chosen_place.append(name[i])
    return Chosen_place
def get_distance(start,finish):
    print(start)
    print(finish)
    key='N87KvQLlqZMH3Q6qSQ2NhCm7zfaNyCr3G1N8n2F6'
    url = "https://rsapi.goong.io/DistanceMatrix?\
        origins={}&destinations={}&vehicle=car&api_key={}".format(start,finish,key)

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data=json.loads(response.text)
    print(data)
    dist=data['rows'][0]['elements'][0]['distance']['value']/1000
    truetime=data['rows'][0]['elements'][0]['duration']['value']
    return [dist,truetime]
Chosen_start=get_place(start_place)
Chosen_end=get_place(end_place)   
min=1e9
for start in Chosen_start:
    for end in Chosen_end:
        p,s=test_class.A_star_search(encode(end), encode(start))
        
        p=p + get_distance((str(start_place[0])+', '+str(start_place[1])), transform(start))[0] \
            + get_distance((str(end_place[0])+', '+str(end_place[1])), transform(end))[0]
        if min>p:
            min=p            
            way=s
print(min) 
for i in s:
    print(i, end='->')            
        
