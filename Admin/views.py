from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"college.html")

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

