# Generated by Django 3.2.9 on 2021-11-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_rename_stopsellpercentage_sell_stop_sell_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='log',
            field=models.TextField(),
        ),
    ]
