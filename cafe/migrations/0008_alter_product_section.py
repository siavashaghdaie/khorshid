# Generated by Django 4.0.1 on 2022-03-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0007_artist_section_product_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='section',
            field=models.CharField(choices=[('painting', 'نفاشی و طراحی'), ('writing', 'خط'), ('sculpture', 'مجسمه'), ('photography', 'عکس'), ('mosaic', 'معرق'), ('fasion', 'طراحی لباس'), ('other', 'دیگر')], max_length=60, null=True, verbose_name='شاخه'),
        ),
    ]
