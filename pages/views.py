from django.shortcuts import render
from django.http import HttpResponse
from pages.models import Page

# Create your views here.
"""

def index(request):
	#return(HttpResponse("<h1>The-meandco-homepage</h1>"))
	return render(request, 'pages/page.html')
	
"""

def index(request,pagename):
	pagename='/'+ pagename
	pg= Page.objects.get(permalink=pagename)
	context={
		'title':pg.title,
		'content':pg.bodytext,
		'last_updated':pg.update_date,
		'page_list':Page.objects.all(),
	}

	return(render(request, 'pages/page.html',context))