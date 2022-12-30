from Calculate_Air import *
import requests
import json
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
    return lat,lng
