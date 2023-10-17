from django.urls import path
from .views import *

urlpatterns = [
    		path('lista-compra/', CompraView),
	    ]