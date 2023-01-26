from django.forms import ModelForm
from .models import Cardapio

class CardapioForm (ModelForm):

    class Meta:
        model = Cardapio
        fields = ('nome', 'preco')