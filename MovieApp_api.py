# *-* coding:utf-8 *-*
import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import json, urllib, unirest
from Fetch_Api import Search_Movie, search_Imdb

# Den här routen + nästa ska vi inte ta med i vår API-dokumentation
@route("/", method="GET")
def index_page():
    return template("index")

@route('/static/<filepath:path>')
def css(filepath):
    return static_file(filepath, root='static')

@route("/search_a_movie/<search_term>", method = "GET")
def call_search_movie(search_term):
    ''' Searches a movie in IMDB's API, and returns list of movies based on the search result. '''

    # Anropa funktion som anropar Imdb API:et
    imdb_list = search_Imdb(search_term)
    print type(imdb_list);

    if type(imdb_list) == list:
        response.content_type = 'application/json'
        response.status = 200
        return json.dumps(imdb_list)
    else:
        error = {}
        response.content_type = 'application/json'
        response.status = 404
        return error

@route("/show_movie/<movie_title>/<movie_year>", method = "GET")
def show_movie(movie_title, movie_year):
    ''' Call Omdb and Youtube API and then return information and trailer for movie to the user '''
    return_data = Search_Movie(movie_title, movie_year)
    omdb_data = return_data[0]
    youtube_video_id = return_data[1]
    youtube_link = "https://www.youtube.com/embed/" + youtube_video_id
    omdb_data['youtube_link'] = youtube_link # Lägger till youtube-länken i omdb-dictionary

    response.content_type = 'application/json'
    return json.dumps(omdb_data)

run(host='localhost', port=8080, debug=True, reloader=True)
