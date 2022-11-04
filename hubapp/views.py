from urllib import request
from django.shortcuts import render
from django.template import engines
from django.http import HttpResponse, HttpResponseRedirect



import requests
import html

# Create your views here.


def test(request):

	return render(request, 'hubapp/test.html') 


def display(request):

    context = {


    }
    return render(request, 'hubapp/display.html', context)

def controller(request):

    context = {

    }

    return render(request, 'hubapp/controller.html', context)

def whereami(request):
	# if request.method == 'GET':
		
	url = "https://www.google.com/maps/dir/?api=1"
	payload = ""
	headers = {
	}
	
	# url2 = "https://www.google.com/recaptcha/api/siteverify"


	response = requests.request("GET", url, headers=headers, data=payload)
	# print(response.text)
	html = response.text
	# print(html)
	django_engine = engines['django']
	template = django_engine.from_string(html)
	# test = lxml.html.fromstring(f'{html}')
	# print(template.render(), 'templates', '----------------------------------------------')
	new_template = template.render()
	context = {
		'stuff': new_template
	}
	# template.render(context)
	# return render(request, 'hubapp/whereami.html', context)
	return HttpResponseRedirect(url)