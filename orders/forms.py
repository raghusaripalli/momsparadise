from django import forms

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'landmark', 'address', 'pincode']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address (Optional)'}),
            'landmark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Landmark (Optional)'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': '3',
                                             'id': 'address'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pincode',
                                              'id': 'pincode'}),
        }
        labels = {
            'name': '', 'phone': '', 'email': '', 'landmark': '', 'address': '', 'pincode': ''
        }
