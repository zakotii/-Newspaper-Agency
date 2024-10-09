from django.db import models

# Модель для темы (Topic)
class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Модель для редактора (Redactor)
class Redactor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Модель для газеты (Newspaper)
class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    redactor = models.ForeignKey(Redactor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
