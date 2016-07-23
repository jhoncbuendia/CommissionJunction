from django.shortcuts import render

# Create your views here.

def create(request):
	return render(request, 'list/create.html')

def view(request):
	return render(request, 'list/view.html')
