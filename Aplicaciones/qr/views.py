from django.shortcuts import render, redirect
from .models import user
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def home(request):
    print("index")
    usuarios = user.objects.all()
    return render(request, "gestion.html", {"usuario": usuarios})


def registrar(request):
    cedulaovariabledeloquesea = request.POST['txtcedula']
    name = request.POST['txtname']
    email = request.POST['txtemail']

    sex = request.POST['txtsex']

    age = request.POST['txtage']
    # country = request.POST['txtcountry']
    country = "Ecuador"
    # city = request.POST['txtcity']
    city = "Quito"
    address = request.POST['txtadd']
    phone = request.POST['txtphone']

    usuario = user.objects.create(
        cedula=cedulaovariabledeloquesea, name=name, email=email, sex=sex, age=age, country=country, city=city, address=address, phone=phone)
    return redirect('/')


def edicion(request, cedula):
    usuario = user.objects.get(cedula=cedula)
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

def datos(request, cedula):
    usuario = user.objects.get(cedula=cedula)
    print(usuario)
    return render(request, "usuario.html", {"usuario": usuario})


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            #register user
            try:
                usuario = User.objects.create_user(
                    username = request.POST['username'],password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('/')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'usuario ya existe'})

            
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'contraseñas no coinciden'})

def signout(request):
    logout(request)
    return redirect("signup")



def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm })
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, usuario)
            return redirect("/")

        
