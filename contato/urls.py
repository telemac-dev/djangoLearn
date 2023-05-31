from django.urls import path
from . import views

urlpatterns = [
    path('contatos/', views.lista_contatos, name='lista_contatos'),
    path('contatos/criar/', views.criar_contato, name='criar_contato'),
    path('contatos/editar/<int:pk>/', views.editar_contato, name='editar_contato'),
    path('contatos/excluir/<int:pk>/', views.excluir_contato, name='excluir_contato'),
]
