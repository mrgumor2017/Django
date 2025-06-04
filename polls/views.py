
from django.shortcuts import render
from .models import Category, Animal

def index(request):
    """
    Головна сторінка сайту
    """
    categories = Category.objects.all()
    animals = Animal.objects.all()[:5]  # Показуємо 5 останніх тварин
    return render(request, 'polls/index.html', {
        'categories': categories,
        'animals': animals
    })

def category_list(request):
    """
    Сторінка зі списком усіх категорій
    """
    categories = Category.objects.all()
    return render(request, 'polls/category_list.html', {
        'categories': categories
    })

def login_view(request):
    return render(request, 'polls/login.html')

def register_view(request):
    return render(request, 'polls/register.html')

def about_view(request):
    return render(request, 'polls/about.html')
