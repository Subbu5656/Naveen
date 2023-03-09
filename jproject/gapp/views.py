from django.shortcuts import render,redirect
from .models import carshowroom
from django.http import HttpResponse
# Create your views here.
def Home(request):
	msg='good morning'
	return HttpResponse(msg)

def Name(request):
	data = cinema.objects.get(id=id)
	return render(request, 'gapp/name.htm', {'data':data})

def Game(request):
	return render(request, 'gapp/name.html')

def Game1(request, id):
	data = cinema.objects.get(id=id)
	return render(request, 'gapp/name1.html', {'data':data})

def Fullname(request):
	if request.method == 'POST':
		emp = carshowroom(
	       car = request.POST['fname'],
	       model = request.POST['lname'])
		emp.save()
	fullname = carshowroom.objects.all()
	return redirect('gapp/home/')

def Delete(request, id):
	data = cinema.objects.get(id=id).delete()
	return redirect('/gapp/home/')

def Update(request, id):
	if request.method == 'POST':
		data = cinema.objects.get(id=id)
		data.car = request.POST['fname']
		data.nomber = request.POST['lname']
		data.save()
	return redirect('/gapp/home/')