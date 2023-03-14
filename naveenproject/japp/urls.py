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
from japp import views
urlpatterns = [
    path('home/', views.Home, name='home'),
    path('name/', views.Name, name='name'),
    path('come/', views.Come, name='come'),
    path('come/<id>/', views.Come1, name = 'name details'),
    path('fullname/', views.Fullname, name='fullname'),
    path('delete/<id>/', views.Delete, name='delete record'),
    path('update/<id>/', views.Update, name='update details'),
]
