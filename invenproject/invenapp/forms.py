from django import forms
from .models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        labels={
            "product_id":'PRODUCT_ID',
            "name":'NAME',
            "sku":'SKU',
            "price":'PRICE',
            "quantity":'QUANTITY',
            "supplier":'SUPPLIER',

        }
        widgets={
            'product_id':forms.NumberInput(attrs={'placeholder':'e.g 1','class':'form-control'}),
            'name':forms.TextInput(attrs={'placeholder':'e.g shirt','class':'form-control'}),

            'sku':forms.TextInput(attrs={'placeholder':'e.g s12345','class':'form-control'}),

            'price':forms.NumberInput(attrs={'placeholder':'e.g Rs.100','class':'form-control'}),

            'quantity':forms.NumberInput(attrs={'placeholder':'e.g 1','class':'form-control'}),

            'supplier':forms.TextInput(attrs={'placeholder':'e.g ABC crop','class':'form-control'}),

        }