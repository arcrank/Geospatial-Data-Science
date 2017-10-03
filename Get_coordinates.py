import folium
import pandas as pd
import usaddress as ua
import requests
import numpy as np


#Import a dataframe that includes Addresses



df = pd.DataFrame([['name1',addr1],['name2',addr2]],columns=['Name','Address']) #example


def get_coordinates(address):

    parsed_address = dict(ua.parse(address))
    ordered_address = {value : key for key,value in parsed_address.items()}
    parts = ordered_address.values()
    addrstr = ''

    for i in parts:
        addrstr= addrstr+ i + '+'

        addrstr=addrstr[:-1]

    response = requests.get(str('https://maps.googleapis.com/maps/api/geocode/json?address='+addrstr))
    resp_json_payload = response.json()
    #print(resp_json_payload['results'][0]['geometry']['location'])
    return(resp_json_payload['results'][0]['geometry']['location'])



coordinates = [np.nan]*len(df)
for ix in df.index:
    try:
        coordinate = get_coordinates(df.loc[ix]['Address'])
        coordinates[ix] = coordinate
    except:
        pass

df['Coordinates'] = coordinates
