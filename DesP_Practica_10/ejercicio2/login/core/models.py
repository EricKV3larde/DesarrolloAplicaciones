from django.db import models

class Usuario(models.Model):
    GENDER_CHOICES = [
        ('male', 'Masculino'),
        ('female', 'Femenino'),
    ]

    INTEREST_CHOICES = [
        ('fiction', 'Ficción'),
        ('action', 'Acción'),
        ('comedy', 'Comedia'),
        ('drama', 'Drama'),
    ]

    HOBBY_CHOICES = [
        ('natacion', 'Natación'),
        ('basket', 'Basket'),
        ('lectura', 'Lectura'),
        ('fulbol', 'Fútbol'),
    ]

    nombre = models.CharField(max_length=255, null = True)
    email = models.EmailField(default='h.gmail.com')
    contraseña = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=6, choices=GENDER_CHOICES)
    interes = models.ManyToManyField('Interes', choices=INTEREST_CHOICES)
    aficiones = models.ManyToManyField('Aficion', choices=HOBBY_CHOICES)
    ciudad = models.CharField(max_length=255)

class Interes(models.Model):
    name = models.CharField(max_length=255, null = True)

class Aficion(models.Model):
    name = models.CharField(max_length=255, null = True)
