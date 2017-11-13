from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new from to create a new bxlog"
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, number):
    print number
    return HttpResponse("placeholder to display blog " + number)

def edit(request, number):
    return HttpResponse("placeholder to edit blog " + number)

def delete(request, number):
    return redirect('/blogs')


