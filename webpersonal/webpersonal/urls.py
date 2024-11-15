from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
 path('', views.home, name="home"),
 path('about-me/', views.about, name="about"),
 path('portfolio/', views.portafolios, name="portfolio"),
 path('contact/', views.contacto, name="contact"),
 path('admin/', admin.site.urls),
]

