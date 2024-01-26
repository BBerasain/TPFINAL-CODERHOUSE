from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from miapp.models import Usuario, Jugadores
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from miapp.forms import UserRegisterForm, UserEditForm



def index(request):
    return render(request, "index.html")

def inicio(request):
    return render(request, "inicio.html")

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request,"inicio.html", {"mensaje":f"Bienvenido {username}"} )
            
            else:
                return render(request,"inicio.html", {"mensaje":"Error, datos incorrectos"} )
        
        else:
            return render(request,"inicio.html", {"mensaje":"Error, formulario erroneo"} )
    
    form = AuthenticationForm()

    return render(request,"login.html", {"form":form} )

def registro(request):

    if request.method == "POST":
        form =  UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request,"inicio.html" , {"mensaje":"se ha creado tu usuario correctamente" })
        
    else:
        form = UserCreationForm()

    return render(request,"registro.html" , {"form":form})

def about_me(request):
    return render(request, "about_me.html")


def traspasos(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        edad = request.POST.get("edad")
        nacionalidad = request.POST.get("nacionalidad")
        ultimo_equipo = request.POST.get("ultimo equipo")
        nuevo_equipo = request.POST.get("nuevo equipo")
        valor_de_traspaso = request.POST.get("valor de traspaso")
        jugador = Jugadores(nombre=nombre,
                            edad=edad,
                            nacionalidad=nacionalidad,
                            ultimo_equipo=ultimo_equipo,
                            nuevo_equipo=nuevo_equipo,
                            valor_de_traspaso=valor_de_traspaso)
        jugador.save()
        return render(request, "traspasos.html")
    return render(request, "traspasos.html")
          
def leerTraspasos(request):
    
    jugadores = Jugadores.objects.all()
    contexto = {"Traspasos":jugadores}
    return render(request, "leerTraspasos.html",contexto)
  

def eliminarTraspaso(request, nombre_jugador):
               
    jugador = get_object_or_404(Jugadores, nombre=nombre_jugador)
    jugador.delete()
    return render(request, "leerTraspasos.html")
