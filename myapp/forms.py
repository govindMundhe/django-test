from django.forms import ModelForm
from django import forms
from .models import Orders, Item
from django.contrib.admin.widgets import AdminDateWidget

def __init__(self, *args, **kwargs):
    user = kwargs.pop('user')
    self.fields['item_name'].queryset = Item.objects.all()
    

class OrderForm (ModelForm):
    item_name = forms.ModelChoiceField(queryset=Item.objects.all(), empty_label='')
    
    class Meta:
            model = Orders
            fields = ['item_name','quantity','added_date','added_time']
            

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item_name','details','price']
    