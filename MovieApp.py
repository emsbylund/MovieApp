
import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app #url
import json, requests
from Fetch_Api import Search_Movie, Call_Ombd_Api

@route("/")
def start_page():
    return template('index')


@route("/search_a_movie", method = "POST")
def call_search_movie():
    ''' Get search from form and call Search_Movie function in Fetch_Api.py '''
    title = request.forms.get('search')
    title.replace(" ", "+")
    print title
    json_movie_data = Search_Movie(title)
    return template("show_result", json_movie_data = json_movie_data)

run(host='localhost', port=8080, debug=True, reloader=True)
