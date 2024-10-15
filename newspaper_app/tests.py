from django.test import TestCase
from django.urls import reverse
from .models import Newspaper, Topic, Redactor

class NewspaperTests(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create(
            first_name='Test', 
            last_name='User', 
            email='testuser@example.com', 
            hire_date='2020-01-01'
        )
        self.topic = Topic.objects.create(name='Politics')

    def test_newspaper_create(self):
        response = self.client.post(reverse('newspaper_create'), {
            'title': 'Test Newspaper',
            'content': 'Test content',
            'published_date': '2024-10-09',
            'publication_date': '2024-10-09',  # Добавляем publication_date
            'topic': self.topic.id,  # Добавляем topic
            'redactor': self.redactor.id,  # Добавляем redactor
            'publishers': [self.redactor.id]  # Поле publishers (если оно требуется)
        })
        
        # Проверяем, был ли перенаправлен ответ
        if response.status_code != 302:
            if response.context and 'form' in response.context:
                print(response.context['form'].errors)  # Выводим ошибки формы, если они есть
            else:
                print("Форма не была найдена в ответе")
        
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Newspaper.objects.filter(title='Test Newspaper').exists())
