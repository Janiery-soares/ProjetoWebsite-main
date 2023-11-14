from django.contrib import admin
from django.urls import path,include
from apps.produtos.views import *
from apps.vendas.views import *
from apps.core.views import *

from django.conf.urls.static import static
from django.conf import settings


# http://127.0.0.1:8000/

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),

    path('', include("apps.core.urls")),
    #path('', include("apps.produtos.urls")), 
]

urlpatterns+= static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)

urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
