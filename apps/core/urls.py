from django.urls import path
from . import views

urlpatterns = [
	path('', views.Home),
    #path('cadastro/', views.Cadastro),
]
