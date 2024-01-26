#Arquivo criado por mim para configurar as urls do projeto
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #Emprestimo
    path('',views.home,name='home'),
    path('novo_emprestimo/',views.novo_emprestimo,name='novo_emprestimo'),
    path('cadastra_novo_emprestimo/',views.cadastra_novo_emprestimo,name='cadastra_novo_emprestimo'),
    path('concluirEmprestimo/<int:pk>',views.concluir_emprestimo_id,name='concluir_emprestimo_id'),
    path('excluirEmprestimo/<int:pk>',views.excluir_emprestimo_id,name='excluir_emprestimo_id'),
    path('editarEmprestimo/<int:pk>',views.editar_emprestimo_id,name='editar_emprestimo_id'),
    path('salvarEmprestimo/<int:pk>',views.editar_emprestimo_id,name='editar_emprestimo_id'),
    #Cliente
    #path('clientes/',views.clientes,name='clientes'),
    #path('excluir_cliente/<int:pk>',views.excluir_cliente_id,name='excluir_cliente_id'),
    #path('cadastrar_novo_cliente/',views.cadastrar_novo_cliente,name='cadastrar_novo_cliente'),

    #Livro
]