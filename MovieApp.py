# *-* coding:utf-8 *-*
import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import json
from Fetch_Api import Search_Movie

# Se över vad vi behöver importera från bottle

@route("/")
def start_page():
    return template('index')

@route("/search_a_movie", method = "POST")
def call_search_movie():
    ''' Get search from form and call Search_Movie function in Fetch_Api.py '''
    title = request.forms.get('search')
    title = title.replace(" ", "+")

    return_data = Search_Movie(title)
    json_movie_data = return_data[0]
    youtube_video_id = return_data[1]
    youtube_video_link = "https://www.youtube.com/embed/" + youtube_video_id

    try:
        return template("show_result", plot = json_movie_data['Plot'], title = json_movie_data['Title'], writer = json_movie_data['Writer'], year = json_movie_data['Year'], youtube_video_link = youtube_video_link)
    except:
        return template("error", message = "Can't find movie. Try again!")


run(host='localhost', port=8080, debug=True, reloader=True)
