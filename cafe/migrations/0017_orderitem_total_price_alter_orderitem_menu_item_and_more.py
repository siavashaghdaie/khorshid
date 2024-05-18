# Generated by Django 4.0.1 on 2022-04-23 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0016_user_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total_price',
            field=models.CharField(max_length=100, null=True, verbose_name='قیمت نهایی'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='menu_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.menuitem', verbose_name='نام محصول'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='تعداد'),
        ),
    ]
