from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def about(request):
       return render(request,"core/about.html")

def contacto(request):
       return render(request,"core/contacto.html")