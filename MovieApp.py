# *-* coding:utf-8 *-*

import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import requests, json

def Call_Api(url):
    base_url="http://omdbapi.com/?"



run(host='localhost', port=8080, debug=True, reloader=True)
