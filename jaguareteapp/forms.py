from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import Customer, Order, Contacto



class OrderForm(ModelForm):
 class Meta:
     model = Order
     fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        
        fields = ['username', 'email', 'password1', 'password2']
        customer = 'username'


class CreateCustomerForm(ModelForm):
     class Meta:
      model = Customer
      fields = '__all__'



class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'
