from django import forms
from .models import articleModel, loginModel

class ArticleForm(forms.ModelForm):
    class Meta:
        model = articleModel
        fields = "__all__"

class loginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = loginModel
        fields = '__all__'