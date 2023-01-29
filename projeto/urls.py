"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from cardapio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="url_index"), 
    path('cadastroCardapio', views.cadastroCardapio, name="url_cadastro"), 
    path('cardapioLista', views.listagemCardapio, name="url_listagem"), 
    path('editar/<int:id>', views.editarCardapio, name="url_editar"), 
    path('delete/<int:id>', views.deleteCardapio, name="url_delete"), 
    path('sobre/', views.sobre, name="url_sobre"),  
    path('busca/', views.search, name="url_busca"),  
    path('account/', include('django.contrib.auth.urls')),
]
