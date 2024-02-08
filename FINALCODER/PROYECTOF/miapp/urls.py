from django.urls import path
from django.contrib.auth.views import LogoutView
from miapp.views import inicio, registro, login_request, index, about_me, traspasos, leerTraspasos, eliminarTraspaso, editarTraspaso


urlpatterns = [
    path("", inicio, name="inicio"),
    path("registro/", registro, name="registro"),
    path("login/", login_request, name="login"),
    path("index/", index, name="index"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("about_me/",about_me, name="about_me"),
    path("traspasos/", traspasos, name="traspasos"),
    path("leerTraspasos/", leerTraspasos, name="LeerTraspasos"),
    path("eliminarTraspaso/<str:nombre_jugador>/", eliminarTraspaso, name="EliminarTraspaso"),
    path("editarTraspaso/<str:nombre_jugador>/", editarTraspaso, name="editarTraspaso"),
]
