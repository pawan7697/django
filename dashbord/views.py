from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashbord(request):

	#text={}
	return render(request,'admin/index.html')

