from django.forms.models import ModelForm
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import ProprieteForm

from .models import Propriete
# Create your views here.

class SubmitPropretyView(CreateView):
    model = Propriete
    ModelForm = ProprieteForm
    fields = ['nom', 'adresse', 'ville', 'code_postal', 'superficie',
         'prix_vente','prix_location','enVente','enLocation', 'description']
    template_name = 'estate/submit-property.html'

    def form_valid(self, form):
        form.instance.agent.user = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Soumettre une propriété'
        return context
