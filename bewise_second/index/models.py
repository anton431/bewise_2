import uuid
from django.core.exceptions import ValidationError
from django.db import models


class Person(models.Model):
    name = models.CharField('Имя', max_length=15, unique=True)
    token = models.UUIDField('Токен пользователя', default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Audio(models.Model):
    audio = models.FileField('Aудио', upload_to='audio/%Y/%m/%d/')
    audio_token = models.UUIDField('Токен аудио', default=uuid.uuid4, editable=False, unique=True)
    person = models.ForeignKey(Person, related_name='person', on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return str(self.audio)

    def clean(self, *args, **kwargs):
        # Не допускаем загрузки не wav.
        if str(self.audio)[-4:] != '.wav':
            raise ValidationError(f'Передайте формат файла .wav, Вы передали {str(self.audio)[-4:]}')

    class Meta:
        verbose_name = 'Аудиозапись'
        verbose_name_plural = 'Аудиозаписи'