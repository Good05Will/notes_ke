from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework import status
from .models import Note


class TestNotesСase(TestCase):
    """Класс тестирования Note"""

    def setUp(self):
        """Настройки теста. Создание тестового пользователя и заметки"""
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.note1 = Note.objects.create(user=self.user,
                                         title='test title1',
                                         text='test text1',
                                         id=1)
        self.note2 = Note.objects.create(user=self.user,
                                         title='test title2',
                                         text='test text2',
                                         id=2)
        self.client = Client()
        self.client.force_login(self.user)

    def test_index(self):
        """Тестирование домашней страницы"""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_notes(self):
        """Тестирование страницы со списком заметок"""
        response = self.client.get('/notes/')
        self.assertEqual(response.status_code, 200)

    def test_note(self):
        """Тестирование страницы отдельной заметки"""
        response = self.client.get('/note/1/')
        self.assertEqual(response.status_code, 200)

    def test_new_note(self):
        """Тестирование страницы создания заметки"""
        response = self.client.get('/new_note/')
        self.assertEqual(response.status_code, 200)

    def test_edit_note(self):
        """Тестирование страницы редактирования заметки"""
        response = self.client.get('/edit_note/1/')
        self.assertEqual(response.status_code, 200)

    def test_api_get(self):
        """Тестирование API для получения всех заметок"""
        response = self.client.get('/api/v1/notes/')
        self.assertEqual(response.status_code, 200)

    def test_api_post(self):
        """Тестирование API создания новой заметки"""
        data = {'title': 'New Note', 'text': 'New text'}
        response = self.client.post('/api/v1/notes/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['note']['title'], data['title'])
        self.assertEqual(response.data['note']['text'], data['text'])
