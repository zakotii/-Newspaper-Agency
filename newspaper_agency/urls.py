from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomeView,
    AdminDashboardView,
    NewspaperListView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    RedactorListView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin_dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/', admin.site.urls),
    path('newspapers/', NewspaperListView.as_view(), name='newspaper_list'),
    path('newspaper/create/', NewspaperCreateView.as_view(), name='newspaper_create'),
    path('newspaper/<int:pk>/update/', NewspaperUpdateView.as_view(), name='newspaper_update'),
    path('newspaper/<int:pk>/delete/', NewspaperDeleteView.as_view(), name='newspaper_delete'),
    path('redactors/', RedactorListView.as_view(), name='redactor_list'),
    path('redactor/create/', RedactorCreateView.as_view(), name='redactor_create'),
    path('redactor/<int:pk>/update/', RedactorUpdateView.as_view(), name='redactor_update'),
    path('redactor/<int:pk>/delete/', RedactorDeleteView.as_view(), name='redactor_delete'),
    path('topics/', TopicListView.as_view(), name='topic_list'),
    path('topic/create/', TopicCreateView.as_view(), name='topic_create'),
    path('topic/<int:pk>/update/', TopicUpdateView.as_view(), name='topic_update'),
    path('topic/<int:pk>/delete/', TopicDeleteView.as_view(), name='topic_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
