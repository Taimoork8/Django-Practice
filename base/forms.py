from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Shop, Warehouse, Product, Student


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['shop_name', 'shop_location']


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        exclude = ['user']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['user']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'student_class', 'profile_pic']

