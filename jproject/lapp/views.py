from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Name(request):
	msg='good ofternoon'
	return HttpResponse(msg)