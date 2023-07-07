from django import forms
from.models import Teacher


class TeacherForms(forms.ModelForm):
    class Meta:
        models=Teacher
        fields="__all__"