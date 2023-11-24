from django.shortcuts import render

from dogs.models import Category, Dog


def index(request):
    context = {
        'objects_list': Category.objects.all()[:3],
        'titles': 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)


def categories(request):
    context = {
        'objects_list': Category.objects.all(),
        'titles': 'Питомник - Все породы'
    }
    return render(request, 'dogs/categories.html', context)


def category_dogs(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'objects_list': Dog.objects.filter(category_id=pk),
        'titles': f'Собаки породы - Все породы {category_item.name}'
    }
    return render(request, 'dogs/dogs.html', context)