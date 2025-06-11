from django.contrib.auth.models import AbstractUser
from django.db import models
from tinymce.models import HTMLField


class CustomUser(AbstractUser):
    image_large = models.ImageField(upload_to='user_images/', null=True, blank=True)
    image_medium = models.ImageField(upload_to='user_images/', null=True, blank=True)
    image_small = models.ImageField(upload_to='user_images/', null=True, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='animals',
        null=True,  # Додано цей параметр
        blank=True  # І цей
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.species}"

    class Meta:
        verbose_name = 'Тварина'
        verbose_name_plural = 'Тварини'

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = HTMLField(verbose_name="Зміст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Автор"
    )

    
    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title