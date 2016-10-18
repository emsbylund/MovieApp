# *-* coding:utf-8 *-*
import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app #url
import json, requests
from Fetch_Api import Search_Movie
import xmltodict
from xmljson import badgerfish as bf
import xml.etree.ElementTree as ET
from collections import OrderedDict

@route("/")
def start_page():
    return template('index')


@route("/search_a_movie", method = "POST")
def call_search_movie():
    ''' Get search from form and call Search_Movie function in Fetch_Api.py '''
    title_omdb = request.forms.get('search')
    # Gör om titeln så att vi den kan användas i URL:en till Trailer Addict API:et:
    title_trailer_addict = title_omdb
    title_trailer_addict = title_trailer_addict.replace(" ", "-")
    # Gör om titeln så att den kan användas i URL:en till OMDB API:et:
    title_omdb = title_omdb.replace(" ", "+")
    return_data = Search_Movie(title_omdb, title_trailer_addict)
    json_movie_data = return_data[0]
    xml_movie_data = return_data[1]


    #TA_to_json = bf.data(ET.fromstring(xml_movie_data))
    #print TA_to_json
    #trailer_link = TA_to_json['trailers']['trailer']['embed_standard']

    # Gammal lösning:
    TA_to_json = xmltodict.parse(xml_movie_data, dict_constructor=dict)
    #print type(TA_to_json)
    print TA_to_json
    #trailer_addict_movie_data = json.dumps(xml_movie_data)
    #print trailer_addict_movie_data
    trailer_link = TA_to_json['trailers']['trailer']['embed_standard']

    try:
        return template("show_result", plot = json_movie_data['Plot'], title = json_movie_data['Title'], writer = json_movie_data['Writer'], year = json_movie_data['Year'], trailer_link = trailer_link)
    except:
        return template("error", message = "Can't find movie. Try again!")


run(host='localhost', port=8080, debug=True, reloader=True)
