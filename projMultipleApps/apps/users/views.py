from django.shortcuts import render, HttpResponse, redirect


def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new from to create a new user record"
    return HttpResponse(response)

def users(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)


