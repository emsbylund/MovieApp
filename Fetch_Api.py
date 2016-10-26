# *-* coding:utf-8 *-*

import json, unirest, urllib

# Kallar på Omdb-API:et.
def Call_Ombd_Api(title_year_encoded):
    base_url = "http://omdbapi.com/?"
    last_part_url = "&plot=short&r=json"
    response = unirest.get(base_url + title_year_encoded + last_part_url)
    if response.code == 200:
        return response.body
    else:
        return "Something went wrong!"

def Call_Youtube_Api(search_keywords):
    ''' Call the youtube API and get the trailer '''
    base_url = "https://www.googleapis.com/youtube/v3/search?q="
    last_part_url = "&part=id,snippet&key=AIzaSyBP7ROoaxopF2QrYJjKyIGNCEyg4fTbJ5A&alt=json&type=video&maxResults=1"
    response = unirest.get(base_url + search_keywords + "+trailer" + last_part_url)
    video_id = response.body['items'][0]['id']['videoId']
    if response.code == 200:
        return video_id
    else:
        return "fel"

def Search_Movie(title, year):
    ''' Calls Omdb and Youtube API to get information about specific movie, and returns it '''
    # For OMDB:
    title_year_encoded = urllib.urlencode({'t': title, 'y': year})
    omdb_movie_data = Call_Ombd_Api(title_year_encoded)
    # For Youtube:
    search_keywords = title + "+" + year
    youtube_video_id = Call_Youtube_Api(search_keywords)

    return omdb_movie_data, youtube_video_id

def Call_Imdb_Api(title):
    base_url = "http://www.imdb.com/xml/find?json=1&tt=on&"
    last_part_url = "%"
    response = unirest.get(base_url + title + last_part_url)
    if response.code == 200:
        print "Från IMDB-API:et får vi detta svaret:"
        print response.body
        print "================================"
        return response.body
    else:
        print "Något gick fel!"

def search_Imdb(title):
    ''' Creates a list of movies from Imdb and return it to call_search_movie in MovieApp.py '''
    title_url_encoded = urllib.urlencode({'q': title})
    print "KODAD TITEL:"
    print title_url_encoded
    json_response = Call_Imdb_Api(title_url_encoded)

    # Get title and year from each movie in Imdb-result and put in list
    correct_movie_list = []

    for movie in json_response['title_popular']:
        movie_dictionary = {}
        movie_dictionary['year'] = str(movie['description'][:4])
        movie_dictionary['title'] = str(movie['title'])
        correct_movie_list.append(movie_dictionary)

    for movie in json_response['title_approx']:
        movie_dictionary = {}
        movie_dictionary['year'] = str(movie['description'][:4])
        movie_dictionary['title'] = str(movie['title'])
        correct_movie_list.append(movie_dictionary)

    return correct_movie_list

    # Kanske endast visa de filmer som faktiskt är filmer, och inte typ intervju-videos osv?
    # Eller endast visa "populära" resultat?

    # Splittar titeln för att kunna jämföra varje ord
    #title_to_compare = title.split(" ")

    # Kontrollerar sökresultatet så att vi endast får resultat där titeln stämmer överens med sökningen
    #for movie in json_response.body['title_popular']:
        #for word in title_to_compare:
            #if word in str(movie['title']):
                #correct_movie_list['title'] = str(movie['title'])
                #correct_movie_list.append(movie['title'])

    #for movie in json_response.body['title_approx']:
        #for word in title_to_compare:
            #if word in str(movie['title']):
                #correct_movie_list['title'] = str(movie['title'])
                #correct_movie_list.append(movie['title'])

    # print correct_movie_list
