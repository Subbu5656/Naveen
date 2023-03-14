"""naveenproject URL Configuration

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
from django.urls import path
from papp import views
urlpatterns = [
    path('home/', views.Home, name='home'),
    path('name/', views.Name, name='name'),
    path('game/', views.Game, name='game'),
    path('game/<id>/', views.Game1, name='game details'),
    path('fullname/', views.Fullname, name='fullname'),
    path('delete/<id>/', views.Delete, name='delete record'),
    path('update/<id>/', views.update, name='update details'),

]