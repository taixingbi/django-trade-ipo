# Generated by Django 3.2.9 on 2021-11-25 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sell',
            old_name='stopSellPercentage',
            new_name='stop_sell_percentage',
        ),
    ]
