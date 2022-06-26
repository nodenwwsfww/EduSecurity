from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import School, Relative, Student


class SchoolForm(forms.ModelForm):
    """Форма школы наследованная от модели школы"""
    class Meta:
        model = School
        fields = '__all__'


class RelativeForm(forms.ModelForm):
    """Форма довереного лица наследованная от модели довереного лица"""
    class Meta:
        model = Relative
        fields = '__all__'


class StudentForm(forms.ModelForm):
    """Форма ученика наследованная от модели ученика"""
    class Meta:
        model = Student
        fields = '__all__'


class RegisterForm(UserCreationForm):
    """Переопределение формы регистрации главного родителя"""
    last_name = forms.CharField(max_length=25, required=False)
    first_name = forms.CharField(max_length=25, required=False)
    patronymic = forms.CharField(max_length=25, required=False)
    city = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=11)
    email = forms.EmailField()
    relative_type = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'phone_number', 'city', 'email']
