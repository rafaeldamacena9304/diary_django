from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Diario
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    postagens = Diario.objects.all().order_by('created_at')[:3]
    pessoas = Pessoa.objects.all()
    nomes = [pessoa.nome for pessoa in pessoas]
    lista_quantidade_nomes = []
    for pessoa in pessoas:
        quantidade = Diario.objects.filter(pessoas = pessoa).count()
        lista_quantidade_nomes.append(quantidade)

    context = {
        'postagens': postagens,
        'nomes': nomes,
        'qtds': lista_quantidade_nomes,
    }
    return render(request, 'home.html', context)

def escrever(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        return render(request, 'escrever.html', {'pessoas': pessoas})
    
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')

        if len(titulo.strip()) == 0 or len(texto.strip()) == 0:
            return redirect('escrever')
        
        diario = Diario(
            titulo = titulo,
            texto = texto,
        )
        diario.save()
        diario.set_tags(tags)

        for id in pessoas:
            pessoa = Pessoa.objects.get(id=id)
            diario.pessoas.add(pessoa)

        diario.save()

        return redirect('escrever')
    
def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'pessoa.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')

        pessoa = Pessoa(
            nome= nome,
            foto= foto
        )
        pessoa.save()

        return redirect('escrever')
    
def dia(request):
    data = request.GET.get('data')
    data_formatada = datetime.strptime(data, '%Y-%m-%d')
    diarios = Diario.objects.filter(created_at__gte=data_formatada).filter(created_at__lte=data_formatada + timedelta(days=1))

    return render(request, 'dia.html', {"diarios": diarios, "total": diarios.count(), "data": data})

def excluir_dia(request):
    data = datetime.strptime(request.GET.get('data'), '%Y-%m-%d')
    diarios = Diario.objects.filter(created_at__gte=data).filter(created_at__lte=data + timedelta(days=1))
    diarios.delete()
    
