from django.shortcuts import render

# Create your views here.
def cmccDemo(request):
	return render(request, 'cmccDemo/home.html')