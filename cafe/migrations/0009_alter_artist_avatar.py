# Generated by Django 4.0.1 on 2022-03-30 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0008_alter_product_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to='', verbose_name='تصویر هنرمند'),
        ),
    ]