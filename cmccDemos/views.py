from django.shortcuts import render, get_object_or_404
from .models import CmccDemo

# Create your views here.
def homepage(request):
	cmccDemos = CmccDemo.objects
	return render(request, 'cmccDemos/home.html', {'cmccDemos': cmccDemos})

def blog(request):
	cmccDemos = CmccDemo.objects
	return render(request, 'cmccDemos/blog.html', {'cmccDemos': cmccDemos})

def contact(request):
	cmccDemos = CmccDemo.objects
	return render(request, 'cmccDemos/contact.html', {'cmccDemos': cmccDemos})

def products(request):
	cmccDemos = CmccDemo.objects
	return render(request, 'cmccDemos/products.html', {'cmccDemos': cmccDemos})

def detail(request, id=None):
	cmccDemo_detail = get_object_or_404(CmccDemo, id=id)
	return render(request, 'cmccDemos/detail.html', {'cmccDemo': cmccDemo_detail})