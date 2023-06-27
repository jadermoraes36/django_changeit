from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def cadastro(request):
    #if request.method == "GET":
    #    return render(request, 'cadastro.html')
    return HttpResponse("Tela Cadastro")