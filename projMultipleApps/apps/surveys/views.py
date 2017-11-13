from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of surveys created"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new from to create a new survey"
    return HttpResponse(response)

