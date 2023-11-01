from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import *
from django.core.files.base import ContentFile, File
from django.contrib import messages
from .models import *
import subprocess


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


def playbook(request):
    taskstatus=1
    task= Task.objects.all()
    return render(request, 'main/playbook.html',{'taskstatus':taskstatus,
                                                 'task':task})
    
def adduser(request):
    
    return render(request,'main/adduser.html')

def deleteuser(request):
    
	return render(request,'main/deleteuser.html')

def lockuser(request):
    
    return render(request,'main/lockuser.html')

def install_sw(request):
    
    return render(request,'main/install_sw.html')

def remove_sw(request):
    
    return render(request,'main/remove_sw.html')

def provision_cluster(request):
    
    return render(request,'main/provision_cluster.html')

def deprovision_cluster(request):
    
    return render(request,'main/deprovision_cluster.html')

def addinventory(request):
    
    return render(request,'main/addinventory.html')

def taginventory(request):
    
    return render(request,'main/taginventory.html')


def execute_usr_ad(request):
    
    if request.method=="POST":
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        cpasswd= request.POST.get('cpasswd')
        inventory= request.POST.get('inventory')
        
        with open('ansible/inventory', 'w') as file:
            file.write(inventory)
	with open(r'ansible/adduser.yml', 'r') as file:
            data = file.read()
        
        data = data.replace('username', username)
        data = data.replace('password', passwd)
        print(data)

        with open(r'ansible/adduser.yml', 'w') as file:
            
            file.write(data)
        task1= 'cd ansible'
        task2 = 'ansible-playbook adduser.yml --extra-vars "username=${username} passwd=${passwd}" '
        subprocess.Popen(task1, shell=True)
        subprocess.Popen(task2, shell=True)
        
        messages.info(request," success!")
        
        return render(request,'main/adduser.html')
         
    return render(request,'main/adduser.html')

