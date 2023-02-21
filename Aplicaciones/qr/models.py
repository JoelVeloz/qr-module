from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # identification = models.TextField(max_length=500, blank=True)
    roles = [
        ('admin', 'Administrador'),
        ('user', 'Usuario'),]
    role = models.CharField(max_length=10, choices=roles, default="user")
    cedula = models.CharField(max_length=10)
    name = models.CharField(max_length=35)
    age = models.PositiveIntegerField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    address = models.CharField(max_length=80)
    email = models.EmailField()
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()