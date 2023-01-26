from django.shortcuts import render,redirect
from .forms import * 
from .models import Cardapio

# Create your views here.
def index(request):
    return render(request, "dashboard.html")

def sobre(request):
    return render(request, "sobre.html")

def cadastroCardapio(request):
    form = CardapioForm(request.POST or None)
    if form.is_valid() :
        form.save()
        return redirect("/cardapioLista") 

    conteudo = {"formulario": form}
    return render(request, 'cadastroCardapio.html', conteudo)

def listagemCardapio(request):
    comidas = Cardapio.objects.all()
    conteudo = {"comidas":comidas}

    return render(request,'listaComidas.html', conteudo)

def editarCardapio (request, id):
    comida = Cardapio.objects.get(pk=id)
    form = CardapioForm(request.POST or None, instance=comida)
    if form.is_valid() :
        form.save()
        return redirect("/cardapioLista") 

    conteudo = {"formulario": form}
    return render(request, 'cadastroCardapio.html', conteudo)


def deleteCardapio(request,id):
    comida = Cardapio.objects.get(pk=id)
    comida.delete()
    return redirect("/cardapioLista")

def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')

    results = Cardapio.objects.filter(nome__icontains=query)
    return render(request, "busca.html", {'query': query, 'results': results})
