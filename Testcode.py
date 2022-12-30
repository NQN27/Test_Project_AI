from Calculate_Air import haversine
import test_class
import requests
import json

matrix = test_class.matrix
name = test_class.name

print(matrix)
#đoạn dưới chưa fix 

def transform_place_to_location():
    place= input()
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
    Chosen_place=[21.02776932801737, 105.83415721961636]
    for i in range(len(name)):
            p=str(location[i][0]).split(',')
            dis=haversine(place[0],place[1],float(p[0]),float(p[1]))
            if dis<=60:
                Chosen_place.append(name[i])
    return Chosen_place
Chosen_start=get_place(start_place)
Chosen_end=get_place(end_place)   

min=1e9
for start in Chosen_start:
    for end in Chosen_end:
        p,q,s=A_star(encode(end), encode(start),0)
        if min>p:
            min=p
            time=q
            way=s
            
        
