from io import BytesIO
from PIL import Image
from django.core.files import File
import uuid
import os

def create_resized_image(img, size, original_name, unique_id):
    """Створює зображення заданого розміру"""
    img_copy = img.copy()
    img_copy.thumbnail(size, Image.Resampling.LANCZOS)
    
    buffer = BytesIO()
    img_copy.save(buffer, 'WEBP', quality=85, optimize=True)
    
    # Додаємо розмір у назву файлу
    size_suffix = f"{size[0]}x{size[1]}"
    new_name = f"{original_name}_{size_suffix}_{unique_id}.webp"
    
    return File(buffer, name=new_name)

def compress_and_convert_to_webp(image):
    """Створює три версії зображення різних розмірів"""
    # Розміри для різних версій
    sizes = {
        'large': (800, 800),
        'medium': (400, 400),
        'small': (200, 200)
    }
    
    # Відкриваємо оригінальне зображення
    img = Image.open(image)
    
    # Генеруємо унікальний ідентифікатор
    unique_id = str(uuid.uuid4())[:8]
    
    # Отримуємо оригінальне ім'я файлу без розширення
    original_name = os.path.splitext(image.name)[0]
    
    # Створюємо різні версії зображення
    image_versions = {}
    
    for size_name, dimensions in sizes.items():
        image_versions[size_name] = create_resized_image(
            img, dimensions, original_name, unique_id
        )
    
    return image_versions