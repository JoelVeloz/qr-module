from django.shortcuts import render, redirect
from .models import user

# Create your views here.


def home(request):
    usuarios = user.objects.all()
    return render(request, "gestion.html", {"usuario": usuarios})


def registrar(request):
    cedula = request.POST['txtcedula']
    name = request.POST['txtname']
    email = request.POST['txtemail']

    sex = request.POST['txtsex']

    age = request.POST['txtage']
    country = request.POST['txtcountry']
    city = request.POST['txtcity']
    address = request.POST['txtadd']
    phone = request.POST['txtphone']

    usuario = user.objects.create(
        cedula=cedula, name=name, email=email, sex=sex, age=age, country=country, city=city, address=address, phone=phone)
    return redirect('/')


def edicion(request, name):
    usuario = user.objects.get(name=name)
    print(usuario)
    return render(request, "editar.html", {"usuario": usuario})

def editar(request):
    cedula = request.POST['txtcedula']
    name = request.POST['txtname']
    email = request.POST['txtemail']
    sex = request.POST['txtsex']
    age = request.POST['txtage']
    country = request.POST['txtcountry']
    city = request.POST['txtcity']
    address = request.POST['txtadd']
    phone = request.POST['txtphone']

    nuevo = user.objects.get(cedula=cedula)
    nuevo.name = name
    nuevo.email = email
    nuevo.sex = sex
    nuevo.age = age
    nuevo.country = country
    nuevo.city = city
    nuevo.address = address
    nuevo.phone = phone
    nuevo.save()
    return redirect('/')


def eliminar(request, cedula):
    usuario = user.objects.get(cedula=cedula)
    usuario.delete()
    return redirect('/')
