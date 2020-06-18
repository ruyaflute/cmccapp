from django.shortcuts import render, get_object_or_404
from .models import CmccDemo

# Create your views here.
def homepage(request):
	cmccDemos = CmccDemo.objects
	return render(request, 'cmccDemos/home.html', {'cmccDemos': cmccDemos})

def blog(request):
	cmccDemo_detail = get_object_or_404(CmccDemo, pk=cmccDemo_id)
	return render(request, 'cmccDemos/blog.html', {})
