from django.contrib.auth.models import User
from django.db import models

from doctors.models import Doctor


# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    id_card_number = models.CharField(max_length=20, verbose_name='ID карт номер')
    phone = models.CharField(max_length=20, verbose_name='Телефон номер')

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациентов'

    def __str__(self):
        return self.user.username

class QueuePatient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Пациент')
    description = models.TextField(verbose_name='Описание')
    accepted = models.BooleanField(verbose_name='Успешность')
    status = models.BooleanField(verbose_name='Статус')
    date_start = models.DateTimeField(verbose_name='Время от')
    date_end = models.DateTimeField(verbose_name='Время до')
    order = models.PositiveIntegerField(verbose_name='Очередь')

    class Meta:
        verbose_name = 'Очередь'
        verbose_name_plural = 'Очередь'

    def __str__(self):
        return self.patient.user.username

