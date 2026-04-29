from django import forms
class form_client(forms.Form):
    names=forms.CharField( max_length=30)
    surnames=forms.CharField( max_length=30)
    dat_ini=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    client_id=forms.IntegerField()
    salary=forms.IntegerField()

class form_search(forms.Form):
    names=forms.CharField( max_length=30, required=False)
    surnames=forms.CharField( max_length=30, required=False)
    client_id=forms.CharField( max_length=30, required=False)
    salary=forms.CharField( max_length=30, required=False)