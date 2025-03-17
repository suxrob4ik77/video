from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Student

class StudentForm(forms.ModelForm):
    title=forms.CharField(max_length=150, label='Malumot',
                          widget=forms.TextInput(attrs={"class": "form-control"}))
    context=forms.CharField(label='Teks',required=False,widget=forms.Textarea(attrs={
        "class":"form-control",
        "rows":5
    }))
    is_bool=forms.BooleanField(label='malumot?',initial=True)
    category=forms.ModelChoiceField(empty_label='Category tanlang',
                                    label='Category',queryset=Student.objects.all(),
                                    widget=forms.Select(attrs={"class": "form-control"}))

class FanlarForm(forms.ModelForm):
    title = forms.CharField(max_length=150, label='Malumot',
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    #
    # class Meta:
    #     model=Student
    #     fi

from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='login',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    class Meta:
        model=User
        fields=('username','password',)


class NewsForm (forms.ModelForm):
    class Meta:
        fields="__all__"

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'lastname', 'phone', 'address', 'email', 'yili', 'fanlar', 'photo', 'video']
