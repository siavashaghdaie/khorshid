# Generated by Django 4.0.1 on 2022-03-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_alter_buy_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='ver',
            field=models.CharField(max_length=6, null=True, verbose_name='کد اعتبار سنجی'),
        ),
    ]