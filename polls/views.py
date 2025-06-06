from django.shortcuts import render, redirect
from .models import Category, Animal, CustomUser
from .forms import CustomUserCreationForm
from django.contrib import messages
from .utils import compress_and_convert_to_webp
from django.views.generic import ListView


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
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.email = form.cleaned_data['email']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                
                if 'image' in request.FILES:
                    # Отримуємо три версії зображення
                    image_versions = compress_and_convert_to_webp(request.FILES['image'])
                    
                    # Зберігаємо кожну версію
                    user.image_large = image_versions['large']
                    user.image_medium = image_versions['medium']
                    user.image_small = image_versions['small']
                
                user.save()
                messages.success(request, 'Ви успішно зареєструвалися!')
                return redirect('polls:index')
            except Exception as e:
                messages.error(request, f'Помилка при реєстрації: {str(e)}')
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'polls/register.html', {'form': form})




def about_view(request):
    return render(request, 'polls/about.html')

class UserListView(ListView):
    model = CustomUser
    template_name = 'polls/user_list.html'
    context_object_name = 'users'
    ordering = ['last_name', 'first_name']