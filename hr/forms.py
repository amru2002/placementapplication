from django import forms
from myapp.models import Category
from myapp.models import Jobs

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mt-3"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mt-3"}))

    
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["name"]
class JobsForm(forms.ModelForm):
    class Meta:
        model=Jobs
        exclude=("status",)
        widgets={
          "category":forms.Select(attrs={"class":"form-control"}),
          "last_date":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }
class JobChangeForm(forms.ModelForm):
    class Meta:
        model=Jobs
        fields="__all__"
        widgets={
          "category":forms.Select(attrs={"class":"form-control"}),
          "last_date":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }

