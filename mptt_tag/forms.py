from django import forms
from mptt_tag.models import Tag

# Definir o número máximo de níveis permitidos
MAX_NIVEIS_HIERARQUIA = 2


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'parent']

    def clean_parent(self):
        parent = self.cleaned_data['parent']

        if parent:
            # Verificar se o nó pai do nó atual possui um número máximo de pais
            n = 1
            while parent.parent:
                n += 1
                parent = parent.parent
                if n > MAX_NIVEIS_HIERARQUIA:
                    raise forms.ValidationError(f"Apenas {MAX_NIVEIS_HIERARQUIA} níveis de hierarquia são permitidos.")

        return parent
