from django.shortcuts import render

# This app is for the sole purpose of showing the home page

def index(request):
    return render(request, 'home/index.html')