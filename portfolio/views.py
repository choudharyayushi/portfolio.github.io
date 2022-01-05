from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index6.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    return render(request, 'contact.html')

