# *-* coding:utf-8 *-*
import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import json, urllib
from Fetch_Api import Search_Movie, search_Imdb

# Se över vad vi behöver importera från bottle

@route("/")
def start_page():
    return template('index')

@route("/search_a_movie", method = "POST")
def call_search_movie():
    ''' Get search words from form and get result from Imdb API '''
    title = request.forms.get('search')

    # Anropa funktion som anropar Imdb API:et
    imdb_list = search_Imdb(title)

    if len(imdb_list) == 1:
        movie_title = imdb_list[0]['title']
        movie_year = imdb_list[0]['year']
        show_movie(movie_title, movie_year)
    elif len(imdb_list) >= 2:
        return template("list_movies", imdb_list = imdb_list)
    else:
        return template("error", message = "Can't find movie. Try again!")

@route("/show_movie/<movie_title>/<movie_year>", method = "GET")
def show_movie(movie_title, movie_year):
    ''' Call Omdb and Youtube API and then present information and trailer for movie to the user '''
    return_data = Search_Movie(movie_title, movie_year)
    omdb_data = return_data[0]
    youtube_video_id = return_data[1]
    youtube_link = "https://www.youtube.com/embed/" + youtube_video_id
    try:
        return template("show_result", plot = omdb_data['Plot'], title = omdb_data['Title'], writer = omdb_data['Writer'], year = omdb_data['Year'], youtube_video_link = youtube_link)
    except:
        return template("error", message = "Something seems to have gone wrong.")

# Ta bort denna??

#@route("/movie_list", method = "POST")
#def movie_list(imdb_list):
    #''' Presents list of movies to the user '''
    #for movie in imdb_list:
        #print movie['title']
        #print movie['year']
    #return template("list_movies", imdb_list = imdb_list)

run(host='localhost', port=8080, debug=True, reloader=True)
