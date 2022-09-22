import sys,os
import splunk.Intersplunk 
import json
import requests as req


def tmdb_api_call(requestURL,parameters):
    response=req.get(url=requestURL,params=parameters)
    if response.status_code !=200:
        print('Status: ',response.status_code,'Headers: ',response.headers,'Error Response: ',response.json())
        exit()
    data=response.json()
    return json.dumps(data)

def get_genre_dtl():
    genres = []
    api_key = "bdde99b87af1105c4ce3803653108dd8"
    requestURL = "https://api.themoviedb.org/3/configuration/languages"
    parameter = {"api_key" : api_key}
    genre_list = tmdb_api_call(requestURL,parameter)
    data = json.loads(genre_list)
    for genre in data:  
        genres.append({"title":genre["english_name"]})       
    return genres


genres = get_genre_dtl()
splunk.Intersplunk.outputResults(genres) 