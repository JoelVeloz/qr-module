from django.shortcuts import render
from .models import user

# Create your views here.

def home(request):
    usuarios = user.objects.all()
    return render(request, "gestion.html", {"usuario": usuarios})