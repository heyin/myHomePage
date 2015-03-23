from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	context          = {}
	context['mainpage'] = 'Hello World!'
	return render(request, 'homepage.html', context)
	# return HttpResponse("hello world!")