from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема')
    description = models.TextField(verbose_name='Короткий описание ')
    read_more = RichTextField( verbose_name='Подробнее')
    image = models.ImageField(upload_to='about/images/', null=True, blank=True, verbose_name='Картинка')


    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title