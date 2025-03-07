from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Directions(models.Model):
    title = models.CharField(max_length=100, verbose_name='')
    description = RichTextField(verbose_name='')
    image = models.ImageField(verbose_name='')

    class Meta:
        verbose_name = "Directions"
        verbose_name_plural = "Directions"

    def __str__(self):
        return self.title


class Doctor(models.Model):
    direction = models.ForeignKey(Directions, on_delete=models.CASCADE, verbose_name='')
    name = models.CharField(max_length=100, verbose_name='')
    description = RichTextField(verbose_name='')
    image = models.ImageField(verbose_name='')
    phone = models.CharField(max_length=20, verbose_name='')
    whatsapp = models.CharField(max_length=255, verbose_name='')
    facebook = models.URLField(verbose_name='')
    instagram = models.URLField(verbose_name='')
    email = models.EmailField(verbose_name='')

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return self.name


class Testimony(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='')
    comment = models.TextField(verbose_name='')
    published = models.BooleanField(default=False, verbose_name='')

    class Meta:
        verbose_name = "Testimony"
        verbose_name_plural = "Testimony"

    def __str__(self):
        return self.doctor.name
