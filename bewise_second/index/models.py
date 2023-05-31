import uuid
from django.core.validators import FileExtensionValidator
from django.db import models


class Person(models.Model):
    name = models.CharField('Имя', max_length=15, unique=True)
    token = models.UUIDField('Токен пользователя', default=uuid.uuid4, editable=False, unique=True, blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Audio(models.Model):
    audio = models.FileField('Aудио', upload_to='audio/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['wav'])])
    audio_token = models.UUIDField('Токен аудио', default=uuid.uuid4, editable=False, unique=True)
    person = models.ForeignKey(Person, related_name='person', on_delete=models.CASCADE, verbose_name='Пользователь',  blank=True)

    def __str__(self):
        return str(self.audio)

    class Meta:
        verbose_name = 'Аудиозапись'
        verbose_name_plural = 'Аудиозаписи'