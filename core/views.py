from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index (request):
	texts = ['lorem ipsum dolor sit amet', 'consectetur adipisicing elit']
	context = {
		'title' : 'django e-commerce',
		'texts' : texts,
	}
	return render(request, 'index.html', context)