from django.db import models


# Create your models here.
class Website(models.Model):
    title = models.CharField(max_length=100, verbose_name='Названия сайта')
    description = models.TextField(verbose_name='Описание')
    keywords = models.TextField(verbose_name='Ключовые слова')
    logo = models.ImageField(verbose_name='Лого')
    phone = models.CharField(max_length=20, verbose_name='Телефон номер')
    email = models.EmailField(verbose_name='Емайл')
    address = models.TextField(verbose_name='Адресс')
    location = models.TextField(verbose_name='Карта')
    instagram = models.TextField(verbose_name='Инстаграм')
    facebook = models.TextField(verbose_name='Файсбук')
    whatsapp = models.TextField(verbose_name='Ватсап')

    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Картинка')
    video = models.TextField(verbose_name='Ссылка на видео из ютуб')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return self.title