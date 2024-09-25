from django.db import models
from django.contrib.auth.models import AbstractUser

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Newspaper, Topic, Redactor
from .forms import NewspaperForm

from django import forms


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Redactor(AbstractUser):
    years_of_experience = models.IntegerField()

    def __str__(self):
        return f"{self.username} ({self.years_of_experience} years)"

class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()
    topics = models.ManyToManyField(Topic)
    publishers = models.ManyToManyField(Redactor)

    def __str__(self):
        return self.title


# Список газет
def newspaper_list(request):
    newspapers = Newspaper.objects.all()
    return render(request, 'newspaper_list.html', {'newspapers': newspapers})

# Создание новой газеты
def newspaper_create(request):
    if request.method == "POST":
        form = NewspaperForm(request.POST)
        if form.is_valid():
            newspaper = form.save()
            return redirect('newspaper_list')
    else:
        form = NewspaperForm()
    return render(request, 'newspaper_form.html', {'form': form})

# Обновление газеты
def newspaper_update(request, pk):
    newspaper = get_object_or_404(Newspaper, pk=pk)
    if request.method == "POST":
        form = NewspaperForm(request.POST, instance=newspaper)
        if form.is_valid():
            form.save()
            return redirect('newspaper_list')
    else:
        form = NewspaperForm(instance=newspaper)
    return render(request, 'newspaper_form.html', {'form': form})


class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ['title', 'content', 'published_date', 'topics', 'publishers']
