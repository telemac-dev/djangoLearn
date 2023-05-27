from django.shortcuts import render, redirect, get_object_or_404
from mptt_tag.models import Tag
from mptt_tag.forms import TagForm

MAX_NIVEIS_HIERARQUIA = 2

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'mptt_tag/tag_list.html', {'tags': tags})

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            parent_id = request.POST.get('parent')
            if parent_id:
                parent = Tag.objects.get(id=parent_id)
                if parent.level + 1 <= MAX_NIVEIS_HIERARQUIA:
                    tag.parent = parent
                else:
                    form.add_error('parent', f"Apenas {MAX_NIVEIS_HIERARQUIA} níveis de hierarquia são permitidos.")
                    return render(request, 'mptt_tag/tag_create.html', {'form': form})
            tag.save()
            return redirect('tag_list')
    else:
        form = TagForm()
    return render(request, 'mptt_tag/tag_create.html', {'form': form})


def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            parent_id = request.POST.get('parent')
            if parent_id:
                parent = Tag.objects.get(id=parent_id)
                if parent.level + 1 <= MAX_NIVEIS_HIERARQUIA:
                    tag.parent = parent
                else:
                    form.add_error('parent', f"Apenas {MAX_NIVEIS_HIERARQUIA} níveis de hierarquia são permitidos.")
                    return render(request, 'tags/tag_update.html', {'form': form, 'tag': tag})
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm(instance=tag)
    return render(request, 'mptt_tag/tag_update.html', {'form': form, 'tag': tag})



def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    
    if request.method == 'POST':
        tag.delete()
        return redirect('tag_list')
    
    return render(request, 'mptt_tag/tag_delete.html', {'tag': tag})


# Create your views here.
def mysite(request):
    return render(request, 'index1.html')

# Create your views here.
