from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    print(request)   # <WSGIRequest: GET '/news/'>
    news = News.objects.all()
    # news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    # ключи из словарей затем используются в качестве переменных в шаблонах
    return render(request, 'mainapp/index.html', context)
    # return render(request, template_name='news/index.html', context=context)






