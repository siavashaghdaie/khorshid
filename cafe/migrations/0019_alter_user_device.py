# Generated by Django 4.0.1 on 2022-04-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0018_order_total_price_alter_orderitem_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='device',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='کد دستگاه'),
        ),
    ]
