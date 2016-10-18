# *-* coding:utf-8 *-*

import requests, json
import xml.etree.ElementTree as ET

# Kallar på Omdb-API:et.
def Call_Ombd_Api(url):
    base_url = "http://omdbapi.com/?"
    response = requests.get(base_url + url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Something went wrong!"

def Call_Trailer_Addict_Api(url):
    base_url = "http://simpleapi.traileraddict.com/"
    print base_url + url
    response = requests.get(base_url + url)
    if response.status_code == 200:
        #tree = ET.parse(response.text) # Gör XML-dokumentet till en sträng
        #root = tree.getroot()
        #print root
        #root = ET.fromstring(response.text)
        #for child in root:
            #print child.tag, child.attrib

# Hanterar sökningsfunktionen på webbplatsen
def Search_Movie(title, title1):
    # För OMDB API:et
    url_omdb = "t=" + title + "&y=&plot=short&r=json"
    json_movie_data = Call_Ombd_Api(url_omdb)
    # För Trailer Addict API:et
    url_trailer_addict = title1 + "/trailer"
    xml_movie_trailer = Call_Trailer_Addict_Api(url_trailer_addict)
    return json_movie_data, xml_movie_trailer
