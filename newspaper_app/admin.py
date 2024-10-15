from django.contrib import admin
from .models import Topic, Redactor, Newspaper

# Регистрируем модели в админке
admin.site.register(Topic)
admin.site.register(Redactor)
admin.site.register(Newspaper)
