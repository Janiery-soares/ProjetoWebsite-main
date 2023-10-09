from django.urls import path
from .views import cadastro, details_blog

urlpatterns = [
    path('blog/', cadastro, name="pagina_cadastro"),
    path('blog/<int:blog_id>', details_cadastro, name="cadastro_detalhes"),

]