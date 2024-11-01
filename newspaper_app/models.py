from django.db import models
from django.utils import timezone


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Redactor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='Content not available')
    published_date = models.DateField(default=timezone.now)
    publication_date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    redactor = models.ForeignKey(Redactor, on_delete=models.CASCADE)
    publishers = models.ManyToManyField('newspaper_app.Redactor', related_name='newspapers')

    def __str__(self):
        return self.title
