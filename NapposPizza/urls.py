from django.contrib import admin
from django.urls import path, include

from apps.biblioteca.views import *
from apps.cadastro.views import *
from apps.core.views import *
from apps.promocoes.views import *
from apps.vendas.views import *

# http://127.0.0.1:8000/

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    path('cadastro/', include('apps.cadastro.urls')),
    path('biblioteca/', include('apps.biblioteca.urls')),
    path('core/', include('apps.core.urls')),
    path('promocoes/', include('apps.promocoes.urls')),
    path('vendas/', include('apps.vendas.urls')),

    # http://127.0.0.1:8000/
    path('', home, name="pagina_home"),
    path('grappelli/', include('grappelli.urls')),
]
