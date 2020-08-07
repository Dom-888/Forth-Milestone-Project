from django.shortcuts import render

# This app has the only purpose of showing the home page
def index(request):
    return render(request, 'home/index.html')