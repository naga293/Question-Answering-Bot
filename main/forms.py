from django import forms
from .models import Question

class QuestionForm(forms.Modelform):
    class Meta:
        model=Question
        fields = ['question','wiki_terms']