from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема')
    description = RichTextField( verbose_name='Описание')
    image = models.ImageField(upload_to='about/images/', null=True, blank=True, verbose_name='Картинка')


    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title