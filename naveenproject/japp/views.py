from django.shortcuts import render,redirect
from .models import cinema
from django.http import HttpResponse
# Create your views here.
def Home(request):
	msg='hiiii naveen kumar'
	return HttpResponse(msg)

def Name(request):
	deta = cinema.objects.all()
	return render(request, 'japp/home.html', {'deta':deta})

def Come(request):
	return render(request,'japp/name.html')

def Come1(request, id):
	data = cinema.objects.get(id=id)
	return render(request, 'japp/name1.html', {'data':data})

def Fullname(request):
	if request.method == 'POST':
		emp=cinema(
			hero=request.POST['fname'],
			vilan=request.POST['lname'])
		emp.save()
	fullname=cinema.objects.all()
	return redirect('/japp/name/')

def Delete(request, id):
	data = cinema.objects.get(id=id).delete()
	return redirect('/japp/name/')

def Update(request, id):
	if request.method == 'POST':
		data = cinema.objects.get(id=id)
		data.hero = request.POST['fname']
		data.vilan = request.POST['lname']
		data.save()
	return redirect('/japp/name/')




