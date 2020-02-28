from django.shortcuts import render
from .models import CmccDemo

# Create your views here.
def homepage(request):
	cmccDemos = CmccDemo.objects
	return render(request, 'cmccDemos/home.html', {'cmccDemos': cmccDemos})

def detail(request, cmccDemo_id):
	print(cmccDemo_id)
	return render(request, 'cmccDemos/home.html')
