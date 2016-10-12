# *-* coding:utf-8 *-*
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
    json_movie_data = Search_Movie(title) # json_movie_data är just nu ett dictionary
    print json_movie_data # bara för testning
    try:
        return template("show_result", plot = json_movie_data['Plot'], title = json_movie_data['Title'], writer = json_movie_data['Writer'], year = json_movie_data['Year'] )
    except:
        return template("error", message = "Can't find movie. Try again!")


run(host='localhost', port=8080, debug=True, reloader=True)
