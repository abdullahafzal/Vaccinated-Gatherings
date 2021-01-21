from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'exposure/index.html')

def about(request):
    return render(request, 'exposure/about.html')

def references(request):
    return render(request, 'exposure/references.html')

def feedback(request):
    return render(request, 'exposure/feedback.html')