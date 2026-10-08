from django.shortcuts import render, redirect, get_object_or_404
from .models import Prenda
from .forms import PrendaForm

def inicio(request):
    return render(request, 'prendas/inicio.html')

def lista_prendas(request):
    prendas = Prenda.objects.all()
    return render(request, 'prendas/lista.html', {'prendas': prendas})


def crear_prenda(request):
    if request.method == 'POST':
        form = PrendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_prendas')
    else:
        form = PrendaForm()

    return render(request, 'prendas/formulario.html', {
        'form': form,
        'titulo': 'Agregar prenda'
    })


def editar_prenda(request, id):
    prenda = get_object_or_404(Prenda, id=id)

    if request.method == 'POST':
        form = PrendaForm(request.POST, instance=prenda)
        if form.is_valid():
            form.save()
            return redirect('lista_prendas')
    else:
        form = PrendaForm(instance=prenda)

    return render(request, 'prendas/formulario.html', {
        'form': form,
        'titulo': 'Editar prenda'
    })


def eliminar_prenda(request, id):
    prenda = get_object_or_404(Prenda, id=id)

    if request.method == 'POST':
        prenda.delete()
        return redirect('lista_prendas')

    return render(request, 'prendas/confirmar_eliminar.html', {
        'prenda': prenda
    })