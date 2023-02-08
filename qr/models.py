from django.db import models

# Create your models here.
class user(models.Model):
    name = models.Charfield(max_length=35)
    email = models.CharField(max_length=100)
    password = models.Charfield(max_length=35)
    role = models.Charfield(max_length=35)
    sexos = [
        ('F','Femenino'),
        ('M','Masculino')
    ]
    sex = models.CharField(max_length=1, choices=sexos, default='F')
    fechaNacimiento = models.DateField()
    age = models.Charfield(max_length=35)
    country = models.Charfield(max_length=35)
    city = models.Charfield(max_length=35)
    address = models.Charfield(max_length=35)
    phone = models.CharField(max_length=10)
    code_qr = models.Charfield(max_length=35)
    
