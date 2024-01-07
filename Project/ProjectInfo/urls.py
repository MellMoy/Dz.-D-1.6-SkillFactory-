"""
Конфигурация URL для проекта DZ_SF_D1.

Список `urlpatterns` направляет URL-адреса в представления. Для получения дополнительной информации см.:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Примеры:
Представления функций
    1. Добавить import:  из представлений import my_app
    2. Добавить URL-адрес в urlpatterns:  path('', views.home, name='home')
Представления на основе классов
    1. Добавить import:  из other_app.views импортировать Home
    2. Добавить URL-адрес в urlpatterns:  path('', Home.as_view(), name='home')
Включение другой конфигурации URL
    1. Импортируйте функцию include(): из django.urls import include, path
    2. Добавить URL-адрес в urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('django.contrib.flatpages.urls')),
]
