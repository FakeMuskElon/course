from django.shortcuts import render
# from django.http import HttpResponse

def homepage(request):
    return render(request, 'home.html')
    # return HttpResponse('<h1>Homepage</h1>')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('My about page')
    