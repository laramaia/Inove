from django.shortcuts import render, redirect

# Create your views here.
from exemplo.forms import SolucaoForm
from exemplo.models import Solucao


def index(request):

    if request.method == 'GET':
        solucoes = Solucao.objects.all()

        form = SolucaoForm()

        context = {
            'solucoes': solucoes,
            'form': form,
        }
        return render(request, 'exemplo/index.html', context)
    
    elif request.method == 'POST':
        form = SolucaoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            solucoes = Solucao.objects.all()

            context = {
                'Solucoes': solucoes,
                'form': form,
            }
            return render(request, 'exemplo/index.html', context)


def update(request, solucao_id):
    if request.method == 'GET':
        solucoes = Solucao.objects.all()
        solucao = Solucao.objects.filter(id=solucao_id).first()
        form = SolucaoForm(instance=solucao)
        context = {
            'solucoes': solucoes,
            'form': form,
        }
        return render(request, 'exemplo/index.html', context)

    elif request.method == 'POST':
        solucao = Solucao.objects.filter(id=solucao_id).first()
        form = SolucaoForm(request.POST, instance=solucao)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            solucoes = Solucao.objects.all()

            context = {
                'solucoes': solucoes,
                'form': form,
            }
            return render(request, 'exemplo/index.html', context)
