from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Directions(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Картинка')

    class Meta:
        verbose_name = "1. Направление"
        verbose_name_plural = "1. Направления"

    def __str__(self):
        return self.title


class Doctor(models.Model):
    direction = models.ForeignKey(Directions, on_delete=models.CASCADE, verbose_name='Направление')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Врач')
    description = RichTextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото')
    phone = models.CharField(max_length=20, verbose_name='Телефон номер')
    whatsapp = models.CharField(max_length=255, verbose_name='Ватсап')
    facebook = models.URLField(verbose_name='Фейсбук')
    instagram = models.URLField(verbose_name='Инстаграм')

    class Meta:
        verbose_name = "2. Врач"
        verbose_name_plural = "2. Врачи"

    def __str__(self):
        return self.user.email


class Testimony(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    comment = models.TextField(verbose_name='Комментарий')
    published = models.BooleanField(default=False, verbose_name='Опубликовать')

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзыв"

    def __str__(self):
        return self.doctor.user.email
