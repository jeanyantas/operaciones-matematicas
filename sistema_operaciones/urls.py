"""sistema_operaciones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_mate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('primos', views.primos, name="primos"),
    path('multiplos', views.multiplos, name="multiplos"),
    path('factorial', views.factorial, name="factorial"),
    path('logaritmo', views.logaritmo, name="logaritmo"),
    path('rPrimo', views.rPrimo, name="rPrimo"),
    path('rMultiplo', views.rMultiplo, name="rMultiplo"),
    path('rFactorial', views.rFactorial, name="rFactorial"),
    path('rLogaritmo', views.rLogaritmo, name="rLogaritmo"),
]
