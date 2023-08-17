from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import *
from django.core.files.base import ContentFile, File
from django.contrib import messages
from .models import *

#####pagination
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)


# Create your views here.


def index(request):
    blogs= Blog.objects.all()
    return render(request, 'main/index.html',{'blogs':blogs})

def logout_request(request):
	logout(request)
	messages.info(request,"Logged out successfully!")
	return redirect("index")

def blog_detail(request, id):
	blog= Blog.objects.get(id=id)
	return render(request,'main/blog_detail.html',{'blog':blog})

def pagination(request):
    # Get page number from request, 
	# default to first page
	default_page = 2
	page = request.GET.get('page', default_page)

	# Get queryset of items to paginate
	items = Blog.objects.all()

	# Paginate items
	items_per_page = 1
	paginator = Paginator(items, items_per_page)

	try:
		items_page = paginator.page(page)
	except PageNotAnInteger:
		items_page = paginator.page(default_page)
	except EmptyPage:
		items_page = paginator.page(paginator.num_pages)

	return render(request, 'main/s.html', {'items_page':items_page})


