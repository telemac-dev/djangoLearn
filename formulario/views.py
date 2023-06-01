from django.shortcuts import render
from .forms import PessoaForm

def formulario(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PessoaForm()
    return render(request, 'formulario/template.html', {'form': form})
