
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
urlpatterns = [
    path('admin/', admin.site.urls),
]
def home(request):
    return HttpResponse("<h1>Bienvenue sur mon site Django !</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),  # Interface d'administration
    path('', home, name='home'),  # Page d'accueil
]
