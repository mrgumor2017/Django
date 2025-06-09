from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from .models import Category, Animal, CustomUser
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages
from .utils import compress_and_convert_to_webp
from django.views.generic import ListView
from .models import Post
from .forms import PostForm
from .forms import LoginForm


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Новину успішно створено!')
            return redirect('polls:post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})



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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Вітаємо, {user.first_name}!')
            return redirect('polls:index')
        else:
            messages.error(request, 'Невірний email/логін або пароль.')
    else:
        form = LoginForm()

    return render(request, 'polls/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('polls:index')


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