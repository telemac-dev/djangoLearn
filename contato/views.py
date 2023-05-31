from django.shortcuts import render, redirect, get_object_or_404
from .forms import PessoaFisicaForm, PessoaJuridicaForm
from .models import PessoaFisica, PessoaJuridica

def lista_contatos(request):
    pessoas_fisicas = PessoaFisica.objects.all()
    pessoas_juridicas = PessoaJuridica.objects.all()
    return render(request, 'contato/lista_contatos.html', {'pessoas_fisicas': pessoas_fisicas, 'pessoas_juridicas': pessoas_juridicas})

def criar_contato(request):
    pessoa_fisica_form = PessoaFisicaForm(request.POST or None)
    pessoa_juridica_form = PessoaJuridicaForm(request.POST or None)

    if request.method == 'POST':
        if request.POST.get('tipo_contato') == 'fisica' and pessoa_fisica_form.is_valid():
            pessoa_fisica_form.save()
            return redirect('lista_contatos')
        elif request.POST.get('tipo_contato') == 'juridica' and pessoa_juridica_form.is_valid():
            pessoa_juridica_form.save()
            return redirect('lista_contatos')

    return render(request, 'contato/criar_contato.html', {'pessoa_fisica_form': pessoa_fisica_form, 'pessoa_juridica_form': pessoa_juridica_form})

def editar_contato(request, pk):
    contato = get_object_or_404(contato, pk=pk)
    pessoa_fisica_form = PessoaFisicaForm(request.POST or None, instance=contato)
    pessoa_juridica_form = PessoaJuridicaForm(request.POST or None, instance=contato)

    if request.method == 'POST':
        if request.POST.get('tipo_contato') == 'fisica' and pessoa_fisica_form.is_valid():
            pessoa_fisica_form.save()
            return redirect('lista_contatos')
        elif request.POST.get('tipo_contato') == 'juridica' and pessoa_juridica_form.is_valid():
            pessoa_juridica_form.save()
            return redirect('lista_contatos')

    return render(request, 'contato/editar_contato.html', {'contato': contato, 'pessoa_fisica_form': pessoa_fisica_form, 'pessoa_juridica_form': pessoa_juridica_form})

def excluir_contato(request, pk):
    contato = get_object_or_404(contato, pk=pk)

    if request.method == 'POST':
        contato.delete()
        return redirect('lista_contatos')

    return render(request, 'contato/excluir_contato.html', {'contato': contato})




def criar_pessoa_fisica(request):
    form = PessoaFisicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_contatos')
    return render(request, 'contato/criar_pessoa_fisica.html', {'form': form})

def criar_pessoa_juridica(request):
    form = PessoaJuridicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_contatos')
    return render(request, 'contato/criar_pessoa_juridica.html', {'form': form})

def editar_pessoa_fisica(request, pk):
    pessoa_fisica = get_object_or_404(PessoaFisica, pk=pk)
    form = PessoaFisicaForm(request.POST or None, instance=pessoa_fisica)
    if form.is_valid():
        form.save()
        return redirect('lista_contatos')
    return render(request, 'contato/editar_pessoa_fisica.html', {'form': form})

def editar_pessoa_juridica(request, pk):
    pessoa_juridica = get_object_or_404(PessoaJuridica, pk=pk)
    form = PessoaJuridicaForm(request.POST or None, instance=pessoa_juridica)
    if form.is_valid():
        form.save()
        return redirect('lista_contatos')
    return render(request, 'contato/editar_pessoa_juridica.html', {'form': form})

def excluir_pessoa_fisica(request, pk):
    pessoa_fisica = get_object_or_404(PessoaFisica, pk=pk)
    if request.method == 'POST':
        pessoa_fisica.delete()
        return redirect('lista_contatos')
    return render(request, 'contato/excluir_pessoa_fisica.html', {'pessoa_fisica': pessoa_fisica})

def excluir_pessoa_juridica(request, pk):
    pessoa_juridica = get_object_or_404(PessoaJuridica, pk=pk)
    if request.method == 'POST':
        pessoa_juridica.delete()
        return redirect('lista_contatos')
    return render(request, 'contato/excluir_pessoa_juridica.html', {'pessoa_juridica': pessoa_juridica})
