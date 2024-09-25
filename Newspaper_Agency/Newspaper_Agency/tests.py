from django.test import TestCase
from django.urls import reverse
from .models import Newspaper, Topic, Redactor

class NewspaperTests(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create(username='testuser', years_of_experience=5)
        self.topic = Topic.objects.create(name='Politics')

    def test_newspaper_create(self):
        response = self.client.post(reverse('newspaper_create'), {
            'title': 'Test Newspaper',
            'content': 'This is a test',
            'published_date': '2024-09-24',
            'topics': [self.topic.id],
            'publishers': [self.redactor.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Newspaper.objects.filter(title='Test Newspaper').exists())
