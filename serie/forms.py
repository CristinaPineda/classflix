from django import forms

from serie.models import Serie

from genero.models import Genero

class SerieForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(SerieForm, self).__init__(*args, **kwargs)
        self.fields["id_idGenero"].label = "Gênero"


    def __init__(self, *args, **kwargs):
        super(SerieForm, self).__init__(*args, **kwargs)
        self.fields["nome"].label = "Insira nova série"

    class Meta:
        model = Serie
        fields = '__all__'
