"""Newspaper_Agency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import home
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", home, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('newspapers/', views.newspaper_list, name='newspaper_list'),
    path('newspaper/create/', views.newspaper_create, name='newspaper_create'),
    path('newspaper/<int:pk>/update/', views.newspaper_update, name='newspaper_update'),
    path('redactors/', views.redactor_list, name='redactor_list'),
    path('topics/', views.topic_list, name='topic_list'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    ]
