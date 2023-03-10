from django.shortcuts import render,redirect
from .models import company
from django.http import HttpResponse
# Create your views here.
def Name(request):
	msg='hiiii good night'
	return HttpResponse(msg) 

def Game(request):
	deta= company.objects.all()
	return render(request, 'bunnyapp/home.html', {'deta':deta})

def Home(request):
	return render(request,'bunnyapp/name.html')

def Home1(request, id):
	deta= company.objects.all()
	return render(request, 'bunnyapp/name1.html', {'deta':deta})

def Fullname(request):
	if request.method == 'POST':
		emp=company(
		  employe=request.POST['fname'],
		  salary=request.POST['lname'])
		emp.save()
	fullname= company.objects.all()
	return redirect('/bunnyapp/game/')

def Delete(request, id):
	data = company.objects.get(id=id).delete()
	return redirect('/bunnyapp/game')

def update(request, id):
	if request.method == 'POST':
		deta = company.objects.get(id=id)
		deta.employe = request.POST['fname']
		deta.salary =  request.POST['lname']
		deta.save()
	return redirect('/bunnyapp/game/')


