from dataclasses import fields
from django.forms import ModelForm
from .models import Buy, Product, User, Artist, OrderItem
from django import forms
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
import cafe


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password','mobile','bio','fav','avatar','address']

class BuyForm(ModelForm):
    
    class Meta:
        model = Buy
        fields = ['order','rec_date','ord_mobile','area','address']
    def __init__(self, *args,**kwargs):
        super(BuyForm,self).__init__(*args,**kwargs)
        self.fields["rec_date"]=JalaliDateField(label=('تاریخ تحویل'),
        widget=AdminJalaliDateWidget)

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','weight', 'stock','des','pic1','pic2','pic3','pic4','posting', 'near_post_price', 'far_post_price']
        

class ArtworkForm(ModelForm):
    class Meta:
        model = Product
        fields = ['artist', 'section', 'name','price','weight', 'stock','des','pic1','pic2','pic3','pic4','posting', 'near_post_price', 'far_post_price']

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['menu_item','quantity']