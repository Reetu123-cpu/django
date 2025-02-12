from django import forms
class Usersform(forms.Form):
    num1=forms.CharField(label="Value 1",required=False)
    num2=forms.CharField(label="Value 2")