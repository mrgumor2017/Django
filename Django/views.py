from django.shortcuts import render

def index(request):
    """
    Головна сторінка сайту
    """
    return render(request, 'index.html')