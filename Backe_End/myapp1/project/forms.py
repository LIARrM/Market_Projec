from  django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . models import Store, CustomUser,CardProduct
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields =  ['username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'avatar','phone_number']

class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']

# class AvatarForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['avatar']

class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'


class CardProductForm(ModelForm):
    class Meta:
        model  = CardProduct
        fields = '__all__'