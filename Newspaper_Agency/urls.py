from django.contrib import admin
from django.urls import path, include
from . import views
from .views import home, admin_dashboard
from django.contrib.auth import views as auth_views
from .views import RedactorUpdateView, RedactorDeleteView, TopicUpdateView, TopicDeleteView, RedactorCreateView, TopicCreateView, TopicListView


urlpatterns = [
    path('newspapers/', views.newspaper_list, name='newspaper_list'),
    path('topic/', TopicListView.as_view(), name='topic_list'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('newspaper/<int:pk>/update/', views.NewspaperUpdateView.as_view(), name='newspaper_update'),
    path('newspaper/<int:pk>/delete/', views.NewspaperDeleteView.as_view(), name='newspaper_delete'),
    # Редакторы
    path('redactor/<int:pk>/update/', RedactorUpdateView.as_view(), name='redactor_update'),
    path('redactor/<int:pk>/delete/', RedactorDeleteView.as_view(), name='redactor_delete'),
    # Темы
    path('topic/<int:pk>/update/', TopicUpdateView.as_view(), name='topic_update'),
    path('topic/<int:pk>/delete/', TopicDeleteView.as_view(), name='topic_delete'),

    path('redactor/create/', RedactorCreateView.as_view(), name='redactor_create'),
    path('topic/create/', TopicCreateView.as_view(), name='topic_create'),

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
