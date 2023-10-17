from django.contrib import admin
from django.urls import path, include

from apps.produtos.views import *
from apps.cadastro.views import *
from apps.vendas.views import *
from apps.core.views import *


# http://127.0.0.1:8000/

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),

    path('cadastro/', CadastroView, name='pagina_cadastro'),

    path('produto/', ProdutosView, name='pagina_produto'),

    path('vendas/', CompraView, name='pagina_vendas'),

    path('core/', FornecedorView, name='pagina_fornecedor'),

]
