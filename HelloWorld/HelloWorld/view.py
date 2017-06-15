from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	# context = {}
	# context['hello'] = 'Hello world!'
	# return render(request, 'hello.html', context)
	return render(request, 'hello.html')

def base(request):
	return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def usersSample(request):
    return render(request, 'usersSample.html')