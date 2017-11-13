from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
import random

def index(request):
    return render(request, 'gold/index.html')

def process_money(request):
    try:
        request.session['totalCoins']
    except KeyError:
        request.session['totalCoins'] = 0

    if request.POST["building"] == "farm":
        farmMoney = random.randrange(10,21)
        request.session["totalCoins"] += farmMoney
        myStr = "Found " + str(farmMoney) + " gold at the farm"


    if request.POST["building"] == "cave":
        caveMoney = random.randrange(5,11)
        request.session["totalCoins"] += caveMoney
        myStr = "Found " + str(caveMoney) + " gold at the cave"


    if request.POST["building"] == "house":
        houseMoney = random.randrange(2,6)
        request.session["totalCoins"] += houseMoney
        myStr = "Found " + str(houseMoney) + " gold at the house"


    if request.POST["building"] == "casino":
        casinoMoney = random.randrange(-50,51)
        request.session["totalCoins"] += casinoMoney
        if casinoMoney < 0:
            myStr = "Lost " + str(abs(casinoMoney)) + " gold at the casino"
        else:
            myStr = "Won " + str(casinoMoney) + " gold at the casino"

    date = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    
    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []

    activity = {}
    activity['name'] = myStr
    activity['date'] = date

    request.session["activities"].append(activity)

    return redirect('/')

