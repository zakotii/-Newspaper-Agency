from django.contrib import admin
from django.urls import path, include
from . import views
from .views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Главная страница
    path("", home, name="home"),

    # Админка
    path('admin/', admin.site.urls),

    # Стандартные пути для авторизации/регистрации через Django
    path('accounts/', include('django.contrib.auth.urls')),

    # Список газет
    path('newspapers/', views.NewspaperListView.as_view(), name='newspaper_list'),

    # Создание новой газеты
    path('newspaper/create/', views.newspaper_create, name='newspaper_create'),

    # Обновление газеты
    path('newspaper/<int:pk>/update/', views.newspaper_update, name='newspaper_update'),

    # Список редакторов
    path('redactors/', views.redactor_list, name='redactor_list'),

    # Список тем
    path('topics/', views.topic_list, name='topic_list'),

    # Logout с перенаправлением на главную страницу
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
