# *-* coding:utf-8 *-*

import json, unirest

# Kallar på Omdb-API:et.
def Call_Ombd_Api(url):
    base_url = "http://omdbapi.com/?"
    response = unirest.get(base_url + url)
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
        "fel"

# Hanterar sökningsfunktionen på webbplatsen.
def Search_Movie(title):
    # För OMDB:
    url_omdb = "t=" + title + "&y=&plot=short&r=json"
    json_movie_data = Call_Ombd_Api(url_omdb)
    # För youtube:
    year = json_movie_data['Year']
    search_keywords = title + "+" + year
    youtube_video_id = Call_Youtube_Api(search_keywords)

    return json_movie_data, youtube_video_id
