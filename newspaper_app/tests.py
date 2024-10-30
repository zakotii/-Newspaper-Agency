from django.test import TestCase
from django.urls import reverse
from .models import Newspaper, Topic, Redactor
from django.contrib.auth import get_user_model


class HomeViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )
        self.client.login(username="testuser", password="password")

        self.topic = Topic.objects.create(name="Test Topic")
        self.redactor = Redactor.objects.create(
            first_name="John", last_name="Doe", email="john@example.com", hire_date="2023-10-10"
        )
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper",
            content="Test content",
            published_date="2024-10-09",
            publication_date="2024-10-09",
            topic=self.topic,
            redactor=self.redactor
        )

    def test_home_view_status(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_home_view_data_counts(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "1")
        self.assertContains(response, "Test Newspaper", msg_prefix="Newspaper title not found")

class NewspaperTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )
        self.client.login(username="testuser", password="password")
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
            'publication_date': '2024-10-09',
            'topic': self.topic.id,
            'redactor': self.redactor.id,
            'publishers': [self.redactor.id]
        })

        # Вывод ошибок формы, если тест не удался
        if response.status_code != 302:
            print("Ошибки формы:", response.context['form'].errors if 'form' in response.context else "Форма не найдена")

        # Проверка кода ответа и успешного создания Newspaper
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Newspaper.objects.filter(title='Test Newspaper').exists())



class NewspaperTests(TestCase):
    def setUp(self):
        # Создаем пользователя для тестов
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )
        self.client.login(username="testuser", password="password")

        # Создаем тестового редактора и тему
        self.redactor = Redactor.objects.create(
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            hire_date='2020-01-01'
        )
        self.topic = Topic.objects.create(name='Politics')

    def test_newspaper_create(self):
        # Тест создания нового объекта Newspaper
        response = self.client.post(reverse('newspaper_create'), {
            'title': 'Test Newspaper',
            'content': 'Test content',
            'published_date': '2024-10-09',
            'publication_date': '2024-10-09',
            'topic': self.topic.id,
            'redactor': self.redactor.id,
            'publishers': [self.redactor.id]
        })

        # Если форма не валидна, выводим ошибки формы
        if response.status_code != 302:
            print("Ошибки формы:", response.context['form'].errors if 'form' in response.context else "Форма не найдена")

        # Проверяем успешное создание объекта Newspaper
        self.assertEqual(response.status_code, 302, "Creation did not redirect")
        self.assertTrue(Newspaper.objects.filter(title='Test Newspaper').exists(), "Newspaper was not created")
