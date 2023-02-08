from django.contrib import admin
from django.urls import path, include
#импортируем функции представления из views.py
from mainapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
#добавляем функции (классы), которые мы создали в представлениях (views.py)
#При запросе пользователя 127.0.0.1:8000/women/ будет срабатывать 
#эта функция-представление
#просто '' - это главная страница
#    path('', index),
#    path('cats/', categories)
#вместо того, чтобы передавать каждую функцию в отдельности, подключаем модуль 
#include - он включает все ссылки, которые обозначены файле urls.py приложения
#этот файл нужно создавать для каждого приложения в отдельности!!
    path('mainapp/', include('mainapp.urls')),
]
