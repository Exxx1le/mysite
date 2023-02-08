#хранение представлений текущего приложения 
from django.shortcuts import render
from django.http import HttpResponse

#представление можно определять через классы или функции. 
# Имя может быть любым. 
# request - ссылка на класс HttpRequest, который содержит параметры запроса.
def index(request):
#функция возвращает экземпляр класса HttpResponce
    return HttpResponse('Страница приложения mainapp')
# после создания фукции её нужно связать с url (по сути с запросом пользователя)
# деляется это через urls.py

def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')