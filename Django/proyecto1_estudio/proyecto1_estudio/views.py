
from django.shortcuts import render
import datetime
import requests
import json

character = 'character/'
episode = 'episode/'
location = 'location/'
pages = '?pages='


def index(request):
	url = 'https://rickandmortyapi.com/api/'+character
	response =  requests.get(url)
	contenido = json.loads(response.content)
	adicional = {"contenido":contenido}
	return render(request,'index.html')

def characters(request):
	url = 'https://rickandmortyapi.com/api/'+character
	response =  requests.get(url)
	contenido = json.loads(response.content)
	adicional = {"contenido":contenido}
	return render(request,'personajes.html',adicional)
