from django.forms import ModelForm
from .models import Propriete


class ProprieteForm(ModelForm):
    class Meta:
        model = Propriete
        fields = ['nom', 'adresse', 'ville', 'code_postal', 'superficie',
         'prix_vente','prix_location','enVente','enLocation', 'description']