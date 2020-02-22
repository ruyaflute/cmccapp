from django.shortcuts import render
from .models import cmccDemo

# Create your views here.
def homepage(request):
	cmccDemos = cmccDemo.objects
	return render(request, 'cmccDemos/home.html', {'cmccDemos': cmccDemos})