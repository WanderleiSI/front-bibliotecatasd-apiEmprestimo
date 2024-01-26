from django.shortcuts import render, redirect
from .models import Emprestimo
from .forms import FormEmprestimo
from django.shortcuts import get_object_or_404
import requests

# Create your views here.
def home(request):
    if request.method == 'GET':
        emprestimo = Emprestimo.objects.all()
        return render(request, 'todo_list.html', {'emprestimo': emprestimo})
    return render(request, 'todo_list.html')

def novo_emprestimo(request):

        responseLiv = requests.get("http://127.0.0.1:8001/livro/")
        responseCli = requests.get("http://127.0.0.1:8002/cliente/")

        json_dataLiv = responseLiv.json()
        json_dataCli = responseCli.json()
        return render(request,'todo_form.html',{'json_dataLiv': json_dataLiv,'json_dataCli': json_dataCli})
    #return render(request, 'todo_form.html', {'formulario': formulario})

def cadastra_novo_emprestimo(request):
    
    if request.method == 'POST':
        
        # Se o formulário foi enviado
        formulario = FormEmprestimo(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            # Se o formulário é válido, salve os dados na model
            emprestimo = Emprestimo(
                titulo=formulario.cleaned_data['titulo'],
                idCliente=formulario.cleaned_data['idCliente'],
                idLivro=formulario.cleaned_data['idLivro'],
                
                dataDevolucao=formulario.cleaned_data['dataDevolucao'],
            )
            emprestimo.save()

            # Redirecione para a página desejada após o sucesso
            return redirect('home')

    else:
        # Se o formulário não foi enviado, crie uma instância do formulário vazio
        formulario = FormEmprestimo()
        
    # Renderize o formulário na página
    return render(request, 'todo_form.html', {'formulario': formulario})

def concluir_emprestimo_id(request, pk):    
    try:
        emprestimo = Emprestimo.objects.get(pk=pk)
        emprestimo.entregue()
        #emprestimo.delete()
    finally:
        return redirect('home')
    

def excluir_emprestimo_id(request, pk):
    try:
        emprestimo = Emprestimo.objects.get(pk=pk)
        emprestimo.delete()
    finally:
        return redirect('home')
    
def editar_emprestimo_id(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)  # Obtenha o objeto Emprestimo com o pk fornecido

    if request.method == 'POST':
        formulario = FormEmprestimo(request.POST, instance=emprestimo)

        if formulario.is_valid():
            formulario.save()
    else:
        formulario = FormEmprestimo(instance=emprestimo)

    responseLiv = requests.get("http://127.0.0.1:8001/livro/")
    responseCli = requests.get("http://127.0.0.1:8002/cliente/")

    json_dataLiv = responseLiv.json()
    json_dataCli = responseCli.json()
    return render(request, 'todo_edit.html', {'formulario': formulario,'json_dataLiv': json_dataLiv,'json_dataCli': json_dataCli})

def novo_cliente(request):
    return render(request,'cliente_form.html')

#Clientes
"""def clientes(request):
    try:
        responseCli = requests.get("http://127.0.0.1:8002/cliente/")

        json_dataCli = responseCli.json()
        return render(request,'cliente_list.html',{'json_dataCli': json_dataCli})
    except:
        pass
    return render(request,'cliente_list.html')

def cadastrar_novo_cliente(request):
    return render(request, 'cliente_form.html')

def excluir_cliente_id(request,pk):
    try:
        responseCli = requests.delete(F"http://127.0.0.1:8002/cliente/{pk}")
    finally:
        return redirect('clientes')"""
    