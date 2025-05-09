from django.shortcuts import render, redirect

# Create your views here.
from demanda.cadastrodemanda.forms import DemandaForm
from demanda.cadastrodemanda.models import Demanda


def index(request):
    if request.method == 'GET':
        demandas = Demanda.objects.all()
        form = DemandaForm()

        context = {
            'demandas': demandas,
            'form': form,
        }
        return render(request, 'demanda/index.html', context)

    elif request.method == 'POST':
        form = DemandaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            demandas = Demanda.objects.all()
            context = {
                'demandas': demandas,
                'form': form,
            }
            return render(request, 'demanda/index.html', context)


def update(request, demanda_id):
    if request.method == 'GET':
        demandas = Demanda.objects.all()
        demanda = Demanda.objects.filter(id=demanda_id).first()
        form = DemandaForm(instance=demanda)

        context = {
            'demandas': demandas,
            'form': form,
        }
        return render(request, 'demanda/index.html', context)

    elif request.method == 'POST':
        demanda = Demanda.objects.filter(id=demanda_id).first()
        form = DemandaForm(request.POST, instance=demanda)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            demandas = Demanda.objects.all()
            context = {
                'demandas': demandas,
                'form': form,
            }
            return render(request, 'demanda/index.html', context)
