# Generated by Django 4.0.1 on 2022-04-24 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0024_alter_menuitem_order_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
