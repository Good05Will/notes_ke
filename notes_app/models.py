from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    '''Модель заметки.'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Возвращает строковое представление модели.'''
        if len(self.title) > 33:
            return f'{self.title[:33]}...'
        else:
            return f'{self.title}'
