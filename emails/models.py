from django.db import models
from django import forms
from django.contrib.auth.models import User

class InterestGroup(models.Model):
    name = models.CharField('grupo', max_length=250)

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    name = models.CharField('Nombre', max_length=250)
    last_name = models.CharField('Apellido Paterno', max_length=250)
    second_last_name = models.CharField('Apellido Materno', max_length=250, blank=True, null=True)
    email = models.EmailField('email')
    degree = models.CharField('Ultimo Grado de Estudios', max_length=250, blank=True, null=True)
    company = models.CharField('Compania', max_length=250, blank=True, null=True)
    interest_groups = models.ManyToManyField(InterestGroup)

    def __str__(self):
        return self.name + " " + self.last_name + " " + self.second_last_name

class SentEmail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField('Asunto', max_length=250)
    interest_groups = models.ManyToManyField(InterestGroup)
    content = models.TextField('Contenido')
    date_sent = models.DateTimeField('Fecha y Hora de Envio', auto_now_add=True)

    def __str__(self):
        return self.subject
