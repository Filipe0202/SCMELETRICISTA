from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Orcamento, Vendedor, Produto
from django.views import generic
from .forms import ProdutoForm, VendedorForm, OrcamentoForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def formulario_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save()
            produto.save()
            return redirect('formulario_produto')
    else:
        form = ProdutoForm()
    return render(request, 'form_produto.html', {'form': form})

def formulario_vendedor(request):
    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            vendedor = form.save()
            vendedor.save()
            return redirect('formulario_vendedor')
    else:
        form = VendedorForm()
    return render(request, 'form_vendedor.html', {'form': form})

def formulario_orcamento(request):
    if request.method == "POST":
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            orcamento = form.save()
            orcamento.save()
            return redirect('formulario_orcamento')
    else:
        form = OrcamentoForm()
    return render(request, 'form_orcamento.html', {'form': form})

class ResultsView(generic.ListView):
    template_name = 'resultado_orcamento.html'
    context_object_name = "lista_orcamentos"

    def get_queryset(self):
        return Orcamento.objects.order_by('id')

class OrcamentoView(generic.DetailView):
    model = Orcamento
    template_name = 'resultado_individual.html'
    context_object_name = 'orcamento'

class ResultsvendedorView(generic.ListView):
    template_name = 'resultado_vendedores.html'
    context_object_name = "vendedor"

    def get_queryset(self):
        return Vendedor.objects.order_by('id')

