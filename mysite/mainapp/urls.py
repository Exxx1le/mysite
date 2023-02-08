from django.urls import path
#импоритруем функции-представления
from .views import *

#в этом списке прописываются все маршруты текущего приложения
urlspatterns = [
    path('', index) #127.0.0.1:8000/women/
#women/ берется из urls.py пакета конфигурации
    path('cats/', categories), #127.0.0.1:8000/women/cats
]