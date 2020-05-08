from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required



def index(request):
	# blogs = Article.objects.all().order_by('date')
	return render(request, 'index.html')


