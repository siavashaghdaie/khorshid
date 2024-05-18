# Generated by Django 4.0.1 on 2022-03-24 08:02

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='نام محصول')),
                ('price', models.CharField(max_length=100, null=True, verbose_name='قیمت محصول')),
                ('weight', models.CharField(max_length=100, null=True, verbose_name='وزن محصول')),
                ('stock', models.CharField(max_length=100, null=True, verbose_name='موجودی محصول')),
                ('des', models.TextField(null=True, verbose_name='توضیحات')),
                ('pic1', models.ImageField(default='product.jpeg', null=True, upload_to='', verbose_name='عکس اصلی')),
                ('pic2', models.ImageField(null=True, upload_to='', verbose_name='عکس دوم')),
                ('pic3', models.ImageField(null=True, upload_to='', verbose_name='عکس سوم')),
                ('pic4', models.ImageField(null=True, upload_to='', verbose_name='عکس چهارم')),
                ('posting', models.TextField(null=True, verbose_name='شرایط ارسال')),
                ('near_post_price', models.CharField(max_length=100, null=True, verbose_name='هزینه ی ارسال نزدیک')),
                ('far_post_price', models.CharField(max_length=100, null=True, verbose_name='هزینه ی ارسال دور')),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=40, verbose_name='نام سفارش دهنده')),
                ('rec_date', models.DateTimeField(verbose_name='تاریخ تحویل')),
                ('ord_mobile', models.CharField(max_length=11, verbose_name='تلفن همراه شما')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت سفارش')),
                ('area', models.CharField(choices=[('one', 'استان تهران یا البرز'), ('two', 'دیگر استان ها')], max_length=20, verbose_name='محدوده')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('shop_type', models.CharField(choices=[('one', 'برای خودم می خرم'), ('two', 'هدیه می دهم')], max_length=20, null=True, verbose_name='نوع خرید')),
                ('rec', models.CharField(max_length=40, null=True, verbose_name='نام گیرنده')),
                ('rec_mobile', models.CharField(max_length=11, null=True, verbose_name='تلفن همراه گیرنده')),
                ('pack_type', models.CharField(choices=[('one', 'به همراه گل'), ('two', 'بدون گل')], max_length=20, null=True, verbose_name='بسته بندی')),
                ('gift_card', models.CharField(max_length=400, null=True, verbose_name='متن  همراه هدیه')),
                ('des', models.TextField(null=True, verbose_name='توضیحات')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.product', verbose_name='محصول')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='ایمیل')),
                ('bio', models.TextField(null=True, verbose_name='درباره ی من')),
                ('fav', models.TextField(null=True, verbose_name='علاقمندی ها')),
                ('mobile', models.CharField(max_length=11, verbose_name='تلفن همراه')),
                ('avatar', models.ImageField(default='avatar.svg', null=True, upload_to='', verbose_name='تصویر')),
                ('mafia_games', models.CharField(max_length=10, null=True, verbose_name='تعداد بازی ها')),
                ('level', models.CharField(max_length=20, null=True, verbose_name='سطح بازی')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]