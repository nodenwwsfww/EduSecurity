from rest_framework import serializers
from .models import School, Relative, Student


class SchoolSerializer(serializers.ModelSerializer):
    """Сериализатор модели школа"""

    class Meta:
        """Определение параметров в мета классе школа"""
        model = School
        fields = ['id', 'region', 'district', 'city', 'school']


class RelativeSerializer(serializers.ModelSerializer):
    """Сериализатор модели родственник"""

    class Meta:
        """Определение параметров в мета классе родственник"""
        model = Relative
        fields = ['id', 'last_name', 'first_name', 'patronymic', 'phone_number', 'email']


class StudentSerializer(serializers.ModelSerializer):
    """Сериализатор модели ученик"""

    class Meta:
        """Определение параметров в мета классе ученик"""
        model = Student
        fields = ['id', 'school', 'parent', 'user_class', 'last_name', 'first_name', 'patronymic', 'phone_number']
