from django.shortcuts import render, HttpResponse, redirect
import random
  # the index function is called when root is visited
def index(request):
    if "gold" not in request.session:
        request.session['list']=[]
        request.session['gold']=0

    return render(request, "app_name/index.html")

def process_money(request):
    if request.POST['building']=="farm":
        request.session['rng']=random.randint(10, 21)
        request.session['gold']+=request.session['rng']
        request.session['list'].append("You earned:"+ str(request.session['rng']))

    if request.POST['building']=="cave":
        request.session['rng']=random.randint(5, 11)
        request.session['gold']+=request.session['rng']
        request.session['list'].append("You earned:"+ str(request.session['rng']))

    if request.POST['building']=="house":
        request.session['rng']=random.randint(2, 6)
        request.session['gold']+=request.session['rng']
        request.session['list'].append("You earned:"+ str(request.session['rng']))

    if request.POST['building']=="casino":
        request.session['rng']=random.randint(-50, 51)
        if request.session['rng']>0:
            request.session['gold']+=request.session['rng']
            request.session['list'].append("You earned:"+ str(request.session['rng']))

        elif request.session['rng']==0:
            request.session['gold']+=request.session['rng']
            request.session['list'].append("You came out even")

        elif request.session['rng']<0:
            temp=request.session['gold']
            temp+=request.session['rng']
            request.session['rng']=request.session['gold']-temp
            request.session['gold']=temp
            request.session['list'].append("You lost:"+ str(request.session['rng']))
    return redirect ('/')

def clear(request):
    request.session.clear()
    return redirect('/')