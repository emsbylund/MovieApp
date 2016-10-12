# *-* coding:utf-8 *-*

#import bottle
#from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import requests, json

# Kallar på Omdb-API:et.
def Call_Ombd_Api(url):
    base_url = "http://omdbapi.com/?"
    response = requests.get(base_url + url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Något gick fel!"

# Hanterar sökningsfunktionen på webbplatsen
def Search_Movie(title):
    url = "t=" + title + "&y=&plot=short&r=json"
    json_movie_data = Call_Ombd_Api(url)
    return json_movie_data
