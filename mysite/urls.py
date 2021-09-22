"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),
    path('boards/', include('boards.urls')),
    path('columns/', include('columns.urls')),
    path('tasks/', include('tasks.urls')),
    path('register/', include('register.urls')),

    path('create_board/', include('boards.urls')),
    path('create_task/', include('tasks.urls')),
    path('create_column/<int:board_id>/', include('columns.urls')),

    path('', include('account_pages.urls')),
    path('', include('django.contrib.auth.urls')),
]
