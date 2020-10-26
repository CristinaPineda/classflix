from django import forms
from genero.models import Genero


class GeneroForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GeneroForm, self).__init__(*args, **kwargs)
        self.fields["descricao"].label = "Insira novo gênero de série"


    class Meta:
        model = Genero
        fields = '__all__'
