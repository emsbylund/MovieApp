# *-* coding:utf-8 *-*

import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import requests, json

def Call_Api(url):
    base_url = "http://omdbapi.com/?"

    response = requests.get(base_url + url)

    try:
        if response.status_code() == 200:
            return response.json()
        else:
            return "Något gick fel!"

def Search_Movie():
    title = "The Notebook"
    title.replace(" ", "+")
    url = "t=" + title + "&y=&plot=short&r=json"

    json_movie_data = Call_Api(url)
    print json_movie_data

Search_Movie()

run(host='localhost', port=8080, debug=True, reloader=True)
