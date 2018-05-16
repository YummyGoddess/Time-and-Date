from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
def yourMethodFromUrls(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p" , gmtime())
    }
    return render(request,"blogs/index.html", context)
# from models import *
  # the index function is called when root is visited
def index(request):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "placeholder to display a new form to creat a new blog"
    return HttpResponse(response)
def create(request):
    if request.method =="POST":
        # print("*"50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = "test"
        # print("*"50)
        return redirect("/")
    else:
        return redirect("/")
