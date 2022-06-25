from django import forms
from .models import School, Relative, Student


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = '__all__'


class RelativeForm(forms.ModelForm):

    class Meta:
        model = Relative
        fields = '__all__'


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
