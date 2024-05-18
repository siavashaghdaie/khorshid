# Generated by Django 4.0.1 on 2022-04-22 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0011_alter_product_artist_alter_product_pic2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=100, null=True, verbose_name='نام دسته')),
                ('pic1', models.ImageField(default='product.jpeg', null=True, upload_to='', verbose_name='عکس')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='نام')),
                ('weight', models.CharField(max_length=100, null=True, verbose_name='وزن')),
                ('des', models.TextField(null=True, verbose_name='توضیحات')),
                ('pic1', models.ImageField(default='product.jpeg', null=True, upload_to='', verbose_name='عکس')),
                ('price', models.CharField(max_length=100, null=True, verbose_name='قیمت')),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.menucat')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('menu_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.menuitem')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.order')),
            ],
        ),
    ]