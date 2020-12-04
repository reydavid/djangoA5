from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    return render(request,"counter/index.html")

def addTwo(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    return redirect('/')

def reset(request):
    if 'counter' not in request.session:
        return redirect('/')
    else:
        request.session['counter'] = 0
        return render(request,"counter/index.html")