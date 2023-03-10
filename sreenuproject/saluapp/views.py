from django.shortcuts import render
from .models import school
from django.http import HttpResponse
# Create your views here.
def Name(request):
	msg='hiiii good morning'
	return HttpResponse(msg)
def Home(request):
	return render(request, 'saluapp/home.html')

def Come(request):
	return render(request, 'saluapp/name.html')

def Fullname(request):
	if request.method == 'POST':
		emp=school(
	        teacher=request.POST['fname'],
	        student=request.POST['lname'])
		emp.save()  
	fullname=school.objects.all()
	return render(request, 'saluapp/fullname.html', {'fullname':fullname})


