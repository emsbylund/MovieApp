# *-* coding:utf-8 *-*
import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import json, urllib, unirest

#@route('/')
#def client_app_index():
    #return template('index')

@route("/search", method = "POST")
def search():
    title = request.forms.get('search')
    new_title = title.replace(' ', '%20')
    url = "http://localhost:8080/search_a_movie/"
    response = unirest.get(url + new_title)
    movie_list = response.body

    if len(movie_list) == 1:
        movie_title = movie_list[0]['title']
        movie_year = movie_list[0]['year']
        display_movie(movie_title, movie_year)
    elif len(movie_list) >= 2:
        return template("list_movies", imdb_list = movie_list)
    else:
        return template("error", message = "Can't find movie. Try again!")

@route("/movie/<movie_title>/<movie_year>", method = "GET")
def display_movie(movie_title, movie_year):
    movie_title = movie_title.replace(" ", "+")
    movie_year = movie_year.replace(" ", "+")
    response = unirest.get("http://localhost:8080/show_movie/" + movie_title + '/' + movie_year)
    json_data = response.body
    try:
        return template("show_result", plot = json_data['Plot'], title = json_data['Title'], writer = json_data['Writer'], year = json_data['Year'], youtube_video_link = json_data['youtube_link'])
    except:
        return template("error", message = "Something seems to have gone wrong.")

run(host='localhost', port=8000, debug=True, reloader=True)
