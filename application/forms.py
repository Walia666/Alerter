from django import forms
from django.forms import ModelForm
from .models import Log
from django.utils.translation import ugettext_lazy as _


class Logform(forms.ModelForm):
        def __init__(self, *args, **kwargs):
        	kwargs.setdefault('label_suffix', '') 
        	super(Logform, self).__init__(*args, **kwargs)
	class Meta:
		model= Log
		fields=['log_field',]
                labels = {
                'log_field': _(''),
                  }
		widgets = {
            'log_field': forms.Select(
                attrs={'onchange': 'myFunction()','class': 'change_select'}
            ),
        }
        
	
		
