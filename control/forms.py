from django import forms

class CuposSudamericana(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    director_tecnico = forms.CharField(required=True, max_length=256)
    capitan = forms.CharField(required=True, max_length=256)
    dorsal = forms.IntegerField(required=True, max_value=99)
