from django.shortcuts import render, HttpResponse
def home(request):
 return render(request, "core/home.html")
def about(request):
 return render(request, "core/about.html")
def portafolios(request):
 return render(request, "core/portfolios.html")
def contacto(request):
 return render(request, "core/contacto.html")