from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib.messages import error


def index(request):
    return render(request, 'users/index.html', { "users": User.objects.all()})

def new(request):
    return render(request, 'users/create.html')

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        
        return redirect('/users/new')

    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
    )
    return redirect('/users')

def show(request, number):
    return render(request, 'users/show.html', { "users": User.objects.get(id=number)})

def edit(request, number):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        
        return redirect('/users/{}/update'.format(number))

    users_to_update = User.objects.get(id=number)
    users_to_update.first_name = request.POST['first_name']
    users_to_update.last_name = request.POST['last_name']
    users_to_update.email = request.POST['email']
    users_to_update.save()
    return redirect('/users')

def update(request, number):
    return render(request, 'users/update.html', { "users": User.objects.get(id=number)})

def delete(request, number):
    User.objects.get(id=number).delete()
    return redirect('/users')


