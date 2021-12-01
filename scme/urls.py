from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario_produto/', views.formulario_produto, name='formulario_produto'),
    path('formulario_vendedor/', views.formulario_vendedor, name='formulario_vendedor'),
    path('formulario_orcamento/', views.formulario_orcamento, name='formulario_orcamento'),
    path('resultado_orcamento/', views.ResultsView.as_view(), name='resultado_orcamento'),
    path('<int:pk>/resultado_individual/', views.OrcamentoView.as_view(), name='resultado_individual'),
    path('<int:pk>/resultado_vendedores/', views.ResultsView.as_view(), name='resultado_vendedores')
]


