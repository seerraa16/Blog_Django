from django.shortcuts import render
from django.shortcuts import render, HttpResponse
# Create your views here.
html_base = """
 <h1>Mi Web Personal</h1>
 <ul>
 <li><a href="/">Portada</a></li>
 <li><a href="/about/">Acerca de</a></li>
 <li><a href="/portafolios/">Portafolios</a></li>
 <li><a href="/contacto/">contacto</a></li>
 </ul>
"""
def home(request):
 return HttpResponse(html_base + """
 <h2>Bienvenidos</h2>
 <p>Esto es la portada.</p>
 """)
def about(request):
 return HttpResponse(html_base + """
 <h2>Acerca de</h2>
 <p>Me llamo Alejandro y me apasiona Django!</p>
 """)

def portafolios(request):
 return HttpResponse(html_base + """
 <h2>Portafolios</h2>
 <p>Este es mi portafolio</p>
 """)

def contacto(request):
 return HttpResponse (html_base + """
    <h2>Contacto</h2>
    <p>Les pongo a continuación mi gmail y mi Linkedin</p>
    <ul>
        <li><a href="mailto:a.serranocatalina@gmail.com">Gmail</a></li>
        <li><a href="https://linkedin.com/in/alejandro-serrano-094145336">Linkedin</a></li>
    </ul>              
                     
 """)