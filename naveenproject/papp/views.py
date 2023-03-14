from django.shortcuts import render,redirect
from .models import family
from django.http import HttpResponse
# Create your views here.
def Home(request):
	msg='hiiii bala chandra'
	return HttpResponse(msg)

def Name(request):
	deta = family.objects.all()
	return render(request,'papp/home.html', {'deta':deta})

def Game(request):
	return render(request,'papp/name.html')

def Game1(request, id):
	deta = family.objects.get(id=id)
	return render(request,'papp/name1.html', {'deta':deta})

def Fullname(request):
	if request.method == 'POST':
		emp=family(
			persons = request.POST['fname'],
			relation= request.POST['lname'])
		emp.save()
	fullname=family.objects.all()
	return redirect('/papp/name/')

def Delete(request, id):
	deta = family.objects.get(id=id).delete()
	return redirect('/papp/name/')

def update(request, id):
	if request.method  == 'POST':
		deta = family.objects.get(id=id)
		deta.persons = request.POST['fname']
		deta.relation = request.POST['lname']
		deta.save()
	return redirect('/papp/name/')

