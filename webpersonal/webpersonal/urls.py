from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
 path('', views.home, name="home"),
 path('about/', views.about, name="about"),
 path('portafolios/', views.portafolios, name="portfolios"),
 path('contacto/', views.contacto, name="contacto"),
 path('admin/', admin.site.urls),
]
