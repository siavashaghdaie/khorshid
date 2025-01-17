# Generated by Django 4.0.1 on 2022-04-01 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0010_product_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.artist', verbose_name='آفریننده'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس دوم'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic3',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس سوم'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic4',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس چهارم'),
        ),
        migrations.AlterField(
            model_name='product',
            name='posting',
            field=models.TextField(blank=True, null=True, verbose_name='شرایط ارسال'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, choices=[('one', 'اثر هنری'), ('two', 'کالای فروشگاهی')], max_length=60, null=True, verbose_name='نوع محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='section',
            field=models.CharField(blank=True, choices=[('painting', 'نفاشی و طراحی'), ('writing', 'خط'), ('sculpture', 'مجسمه'), ('photography', 'عکس'), ('mosaic', 'معرق'), ('fasion', 'طراحی لباس'), ('other', 'دیگر')], max_length=60, null=True, verbose_name='شاخه'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='موجودی محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='وزن محصول'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='درباره ی من'),
        ),
    ]
