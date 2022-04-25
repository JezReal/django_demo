from django.forms import Form
from django import forms


class StudentForm(Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    age = forms.IntegerField()
