#from typing_extensions import Required
from itertools import product
from re import T
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from django_jalali.db import models as jmodels

area = (
    ('one', 'استان تهران یا البرز'),
    ('two', 'دیگر استان ها')
)

shop_type = (
    ('one', 'برای خودم می خرم'),
    ('two', 'هدیه می دهم')
)

pack_type = (
    ('one', 'به همراه گل'),
    ('two', 'بدون گل')
)

product_type = (
    ('one', 'اثر هنری'),
    ('two', 'کالای فروشگاهی')
)

art_section=(
    ('painting', 'نفاشی و طراحی'),
    ('writing', 'خط'),
    ('sculpture', 'مجسمه'),
    ('photography', 'عکس'),
    ('mosaic', 'معرق'),
    ('fasion', 'طراحی لباس'),
    ('other', 'دیگر'),
)

class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام هنرمند',null=True)
    section = models.CharField(max_length=100, verbose_name='دسته ی هنری',null=True)
    avatar = models.ImageField(null=True, default="avatar.svg", verbose_name='تصویر هنرمند')
    des = models.TextField( verbose_name='مشخصات',null=True)
    def __str__(self) -> str:
        return self.name
        
class User(AbstractUser):
    email = models.EmailField(verbose_name='ایمیل',null=True ,blank=True)
    bio = models.TextField(null = True,verbose_name='درباره ی من',blank=True)
    address = models.TextField(null = True,verbose_name='آدرس',blank=True)
    fav = models.TextField(null = True,verbose_name='علاقمندی ها',blank=True)
    mobile = models.CharField(max_length=11, null=True, verbose_name='تلفن همراه',blank=True)
    avatar = models.ImageField(null=True, default="avatar.svg", verbose_name='تصویر',blank=True)
    mafia_games = models.CharField(max_length=10, null=True, verbose_name='تعداد بازی ها',blank=True)
    level = models.CharField(max_length=20, null=True, verbose_name='سطح بازی',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    device = models.CharField(max_length=100, null=True, verbose_name='کد دستگاه',blank=True)
    #telling django to use e-mail instead of username
    #USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Customer(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        if self.name:
            name =  self.name
        else:
            name = self.device
        return str(name)


class Product(models.Model):

    artist = models.ForeignKey (Artist, on_delete=models.SET_NULL, null=True, verbose_name='آفریننده',blank=True)
    section = models.CharField(max_length=60, choices=art_section, verbose_name='شاخه', null=True,blank=True)
    product_type = models.CharField(max_length=60, choices=product_type, verbose_name='نوع محصول', null=True,blank=True)
    name = models.CharField(max_length=100, verbose_name='نام محصول',null=True)
    price = models.CharField(max_length=100, verbose_name='قیمت محصول',null=True)
    weight = models.CharField(max_length=100, verbose_name='وزن محصول',null=True,blank=True)
    stock = models.CharField(max_length=100, verbose_name='موجودی محصول',null=True,blank=True)
    des = models.TextField( verbose_name='توضیحات',null=True)
    pic1 = models.ImageField(verbose_name='عکس اصلی',null=True, default='product.jpeg')
    pic2 = models.ImageField(verbose_name='عکس دوم',null=True,blank=True)
    pic3 = models.ImageField(verbose_name='عکس سوم',null=True,blank=True)
    pic4 = models.ImageField(verbose_name='عکس چهارم',null=True,blank=True)
    posting = models.TextField( verbose_name='شرایط ارسال',null=True,blank=True)
    near_post_price = models.CharField(max_length=100, verbose_name='هزینه ی ارسال نزدیک',null=True)
    far_post_price = models.CharField(max_length=100, verbose_name='هزینه ی ارسال دور',null=True)
    def __str__(self):
        return self.name


class Buy(models.Model):
    objects = jmodels.jManager()
    product = models.ForeignKey (Product, on_delete=models.SET_NULL, null=True, verbose_name='محصول')
    order = models.CharField(max_length=40, verbose_name='نام سفارش دهنده')
    rec_date = models.DateTimeField(verbose_name='تاریخ تحویل')
    ord_mobile = models.CharField(max_length=11, verbose_name='تلفن همراه شما')
    order_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت سفارش')
    update_time = models.DateTimeField(auto_now=True,verbose_name='زمان بروز رسانی')
    area = models.CharField(max_length=20, choices=area, verbose_name='محدوده', default='استان تهران یا البرز')
    address = models.TextField( verbose_name='آدرس')
    shop_type = models.CharField(max_length=20, choices=shop_type, verbose_name='نوع خرید',null=True)
    rec = models.CharField(max_length=40, verbose_name='نام گیرنده',null=True)
    rec_mobile = models.CharField(max_length=11, verbose_name = 'تلفن همراه گیرنده',null=True)
    pack_type = models.CharField(max_length=20, choices=pack_type, verbose_name='بسته بندی',null=True)
    gift_card = models.CharField(max_length=400, verbose_name='متن  همراه هدیه',null=True)
    des = models.TextField( verbose_name='توضیحات',null=True)
    ver = models.CharField(max_length=6, verbose_name='کد اعتبار سنجی',null=True)
    satteled = models.BooleanField (default=False)
    def __str__(self) -> str:
        return self.order

class MenuCat(models.Model):
    cat = models.CharField(max_length=100, verbose_name='نام دسته', null=True)
    pic1 = models.ImageField(verbose_name='عکس',null=True, default='product.jpeg')
    def __str__(self) -> str:
        return self.cat

class MenuItem(models.Model):
    cat = models.ForeignKey(MenuCat, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, verbose_name='نام', null=True)
    weight = models.CharField(max_length=100, verbose_name='وزن', null=True)
    des = models.TextField( verbose_name='توضیحات',null=True)
    pic1 = models.ImageField(verbose_name='عکس',null=True, default='product.jpeg')
    price = models.CharField(max_length=100, verbose_name='قیمت',null=True)
    order_item = models.ForeignKey( 'OrderItem', default=0, verbose_name='سفارش', on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    total_price = models.CharField(max_length=100, verbose_name='قیمت نهایی فاکتور',null=True)
    def __str__(self):
        return(str(self.id))

class OrderItem(models.Model):
    menu_item = models.ForeignKey(MenuItem,verbose_name='نام محصول', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0,verbose_name='تعداد', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    total_price = models.CharField(max_length=100, verbose_name='قیمت نهایی محصول',null=True)
    def __str__(self):
        return str(self.id)


