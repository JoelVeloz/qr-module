from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user(models.Model):
    custom_id = models.AutoField(primary_key=True)
    cedula = models.CharField( max_length=10 )
    name = models.CharField(max_length=35)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=35)
    role = models.CharField(max_length=35)
    sexos = [
        ('F','Femenino'),
        ('M','Masculino')
    ]
    sex = models.CharField(max_length=1, choices=sexos, default='F')
    #fechaNacimiento = models.DateField()
    age = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    address = models.CharField(max_length=35)
    phone = models.CharField(max_length=10)
    code_qr = models.CharField(max_length=35)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.name,self.cedula)
    
