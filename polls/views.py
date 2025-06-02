from django.shortcuts import render
from .models import Category

def index(request):
    categories = Category.objects.all()
    return render(request, 'polls/category_list.html', {'categories': categories})