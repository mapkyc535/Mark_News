from django.shortcuts import render
from main.models import News, Category


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'список новостей',
    }
    return render(request, template_name='main/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'main/category.html', {'news': news, 'category': category})
