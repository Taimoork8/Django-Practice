# serializers.py
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format='%d %b,%Y, %H:%M %p')

    class Meta:
        model = Student
        fields = '__all__'
