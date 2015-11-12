'''
Created on 28 de oct. de 2015

@author: PC1
'''
from django import forms
from .models import Match
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineRadios, Div
from crispy_forms.layout import Layout
from django.utils.translation import ugettext_lazy as _

class MatchForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
             Div(
                Div(InlineRadios('Real_Madrid'),css_class='col-md-6',),
                Div('away_team',css_class='col-md-6', id='team',),
            ),
            Div(
                Div('match_day',css_class='col-md-6',),
                Div('referee',css_class='col-md-6', id='referee',),
            ),                       
        )
        
    class Meta:
        model = Match
        fields = ('Real_Madrid', 'away_team', 'match_day', 'referee')
        labels = {
            'away_team': _('vs')
        }
        
        
        