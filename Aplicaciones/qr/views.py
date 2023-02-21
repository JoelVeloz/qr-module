from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
# from .forms import SignUpForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required


# def home(request):
#     print("index")
#     # usuarios = user.objects.all()
#     return render(request, "a.html")


@login_required
def dashboard(request):
    data = {}
    n_usuarios = User.objects.all().count()
    data['n_usuarios'] = n_usuarios

    return render(request, "dashboard.html", {"data": data})


@login_required
def home(request):
    print("index")
    usuarios = User.objects.all().select_related('profile')
    return render(request, "gestion.html", {"usuario": usuarios})

# @login_required
# def home(request):
#     print("index")
#     return render(request, "home.html")

# @login_required


def registrar(request):
    cedulaovariabledeloquesea = request.POST['txtcedula']
    name = request.POST['txtname']
    email = request.POST['txtemail']

    password = request.POST['txtpass']
    # usuario = User.objects.create(
    #     password=password,
    #     username=email,
    # )
    # print(usuario)
    # # usuario.save()
    # perfil = Profile.objects.create(
    #     user=usuario,
    #     bio=cedulaovariabledeloquesea,
    # )
    usuario = User.objects.create_user(
        username=email, password=password)

    usuario.profile.bio = cedulaovariabledeloquesea
    usuario.save()
    return redirect('/')


@login_required
def edicion(request, id):
    usuario = User.objects.get(id=id)
    print(usuario)
    return render(request, "editar.html", {"usuario": usuario})


@login_required
def editar(request):
    id = request.POST['id']
    cedula = request.POST['txtcedula']
    name = request.POST['txtname']
    print(cedula)
    print("---------------------------------------")
    # email = request.POST['txtemail']
    # sex = request.POST['txtsex']
    # age = request.POST['txtage']
    # country = request.POST['txtcountry']
    # city = request.POST['txtcity']
    # address = request.POST['txtadd']
    # phone = request.POST['txtphone']

    nuevo = User.objects.get(id=id)
    nuevo.username = name
    nuevo.profile.bio = cedula
    # nuevo.email = email
    # nuevo.sex = sex
    # nuevo.age = age
    # nuevo.country = country
    # nuevo.city = city
    # nuevo.address = address
    # nuevo.phone = phone
    nuevo.save()
    return redirect('/')


@login_required
def eliminar(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('/')


@login_required
def datos(request, id):
    usuario = User.objects.get(id=id)
    return render(request, "usuario.html", {"usuario": usuario})


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])

                usuario.profile.bio = "hola"

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
    return redirect('gestion:signin')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'})
        else:
            login(request, usuario)
            # usuario.profile.role = "admin"
            # if(usuario.profile.role == "admin"):
            #     return redirect('gestion:dashboard')
            # else:
            return redirect("/")


def error_404_view(request, exception):
    return render(request, 'error_404.html')
